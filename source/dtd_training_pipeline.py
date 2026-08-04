import argparse
import json
import logging
import os
from typing import Dict, Iterable, List, Tuple


DEFAULT_INPUT_FILE = "./policy-docs/neo-policy-poc-main/unified_dtd_data.json"
DEFAULT_OUTPUT_FILE = "./training_data/dtd_train.jsonl"
DEFAULT_LOG_FILE = "./dtd_pipeline.log"


def configure_logger(log_file: str) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler(),
        ],
    )


def load_json_file(filepath: str) -> Dict:
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)


def is_tag_entry(name: str, payload: Dict) -> bool:
    if not isinstance(payload, dict):
        return False
    if not name:
        return False
    # Keep real DTD tags only; skip grouped documentation keys.
    if name.lower() != name:
        return False
    if "_" in name:
        return False
    allowed_chars = set("abcdefghijklmnopqrstuvwxyz0123456789-")
    return set(name).issubset(allowed_chars)


def select_tag_entries(data: Dict) -> List[Tuple[str, Dict]]:
    tags = [(name, payload) for name, payload in data.items() if is_tag_entry(name, payload)]
    tags.sort(key=lambda item: item[0])
    return tags


def make_tag_definition_record(tag_name: str, payload: Dict) -> Dict[str, str]:
    """Create a record that teaches tag definition, purpose, and metadata."""
    description = (payload.get("description") or "").strip()
    content = (payload.get("content") or "").strip()
    parents = payload.get("parents") or []
    children = payload.get("children") or {}

    definition_text = f"Define the DirXML DTD tag <{tag_name}>."
    
    output_lines = [
        f"Tag: <{tag_name}>",
        f"Purpose: {description}" if description else f"Purpose: {tag_name} element in DirXML",
        f"Content Model: {content if content else 'EMPTY'}",
    ]
    
    if parents:
        output_lines.append(f"Valid Parent Elements: {', '.join(parents)}")
    
    if children:
        child_list = ", ".join(sorted(children.keys())[:10])  # Limit to 10 for readability
        if len(children) > 10:
            child_list += f", ... and {len(children) - 10} more"
        output_lines.append(f"Valid Child Elements: {child_list}")

    return {
        "instruction": definition_text,
        "output": "\n".join(output_lines),
    }


def make_attribute_record(tag_name: str, payload: Dict) -> Dict[str, str]:
    """Create a record teaching about tag attributes and their usage."""
    instruction = f"What attributes can <{tag_name}> accept? List required and optional attributes."
    
    # Extract attributes from metadata if available
    output_lines = [f"Attributes for <{tag_name}>:"]
    
    # Common attributes from DirXML DTD
    common_attrs = {
        "mode": "Comparison mode (case, nocase, default)",
        "op": "Operator (equal, not-equal, less-than, greater-than, etc.)",
        "name": "Attribute or variable name",
        "scope": "Scope level (policy, global, operation)",
        "type": "Data type specification",
        "disabled": "Boolean to disable rule/condition",
    }
    
    relevant_attrs = {k: v for k, v in common_attrs.items() if k in str(payload)}
    
    if relevant_attrs:
        output_lines.append("Common attributes for this tag:")
        for attr, desc in relevant_attrs.items():
            output_lines.append(f"  - {attr}: {desc}")
    else:
        output_lines.append("This tag may not have attributes, or uses child elements for parameters.")
    
    return {
        "instruction": instruction,
        "output": "\n".join(output_lines),
    }


def make_when_to_use_record(tag_name: str, payload: Dict) -> Dict[str, str]:
    """Create a scenario-based record asking when and why to use the tag."""
    description = (payload.get("description") or "").strip()
    parents = payload.get("parents") or []
    
    instruction = f"When would you use the <{tag_name}> tag in a DirXML policy? Describe the scenario and context."
    
    output_lines = [f"When to use <{tag_name}>:"]
    
    if description:
        output_lines.append(f"Purpose: {description[:150]}")
    
    if parents:
        output_lines.append(f"Context: This tag is used within: {', '.join(parents)}")
        output_lines.append(f"Example scenarios where {tag_name} is useful:")
        
        if "rule" in parents or "actions" in parents:
            output_lines.append("  - When defining transformation logic in policies")
            output_lines.append("  - When processing identity management operations")
        
        if "conditions" in parents or "and" in parents or "or" in parents:
            output_lines.append("  - When evaluating prerequisites before executing actions")
            output_lines.append("  - When building complex conditional logic")
    
    return {
        "instruction": instruction,
        "output": "\n".join(output_lines),
    }


def make_valid_combination_record(tag_name: str, payload: Dict) -> Dict[str, str]:
    """Create a record teaching valid tag combinations and hierarchies."""
    parents = payload.get("parents") or []
    children = payload.get("children") or {}
    
    instruction = f"Show a valid XML combination using <{tag_name}> with its parent and child elements."
    
    output_lines = [f"Valid tag combinations with <{tag_name}>:"]
    output_lines.append("")
    
    # Build example based on parent context
    if parents:
        parent = parents[0]
        output_lines.append(f"<{parent}>")
        output_lines.append(f"  <{tag_name}>")
        
        if children:
            child_keys = list(children.keys())[:2]
            for child in child_keys:
                output_lines.append(f"    <{child}/>")
        else:
            output_lines.append(f"    <!-- content here -->")
        
        output_lines.append(f"  </{tag_name}>")
        output_lines.append(f"</{parent}>")
    else:
        output_lines.append(f"<{tag_name}>")
        if children:
            child_keys = list(children.keys())[:2]
            for child in child_keys:
                output_lines.append(f"  <{child}/>")
        output_lines.append(f"</{tag_name}>")
    
    return {
        "instruction": instruction,
        "output": "\n".join(output_lines),
    }


def make_error_detection_record(tag_name: str, payload: Dict) -> Dict[str, str]:
    """Create a record teaching error detection for invalid tag usage."""
    parents = payload.get("parents") or []
    children = payload.get("children") or {}
    
    instruction = f"Identify what's wrong with this XML usage of <{tag_name}> and explain the correct usage."
    
    # Generate invalid example
    invalid_lines = []
    if parents and parents[0] != tag_name:
        # Wrong parent context
        wrong_parent = "policy" if parents[0] != "policy" else "rule"
        invalid_lines.append(f"<{wrong_parent}>")
        invalid_lines.append(f"  <{tag_name}/>")
        invalid_lines.append(f"</{wrong_parent}>")
    else:
        invalid_lines.append(f"<{tag_name}>")
        invalid_lines.append(f"  <invalid-child/>")
        invalid_lines.append(f"</{tag_name}>")
    
    invalid_xml = "\n".join(invalid_lines)
    
    output_lines = [
        "Problem:",
        "The above usage is incorrect. Here's why:",
        f"- <{tag_name}> should appear under: {', '.join(parents) if parents else 'specific parent elements'}",
        f"- Valid child elements are: {', '.join(list(children.keys())[:5]) if children else 'see content model'}",
        "",
        "Corrected Usage:",
        f"<{parents[0] if parents else tag_name}>",
        f"  <{tag_name}/>",
        f"</{parents[0] if parents else tag_name}>",
    ]
    
    return {
        "instruction": instruction,
        "input": invalid_xml,
        "output": "\n".join(output_lines),
    }


def make_qa_record(tag_name: str, payload: Dict) -> Dict[str, str]:
    """Create Q&A records for tag understanding."""
    description = (payload.get("description") or "").strip()
    
    questions = [
        f"What is the purpose of the <{tag_name}> tag in DirXML?",
        f"In what contexts can you use <{tag_name}>?",
        f"What are the child elements allowed within <{tag_name}>?",
        f"Can <{tag_name}> appear directly under a <policy> element?",
    ]
    
    # Return first applicable question
    question = questions[0]
    answer = description if description else f"{tag_name} is a DirXML DTD element used for policy definition and management."
    
    return {
        "instruction": question,
        "output": answer,
    }


def make_example_record(tag_name: str, payload: Dict) -> Dict[str, str]:
    """Create a record showing practical usage examples of the tag."""
    parents = payload.get("parents") or []
    children = payload.get("children") or {}
    description = (payload.get("description") or "").strip()
    
    instruction = f"Provide a real-world example of using <{tag_name}> in a DirXML policy."
    
    example_lines = [f"Example usage of <{tag_name}>:"]
    example_lines.append("")
    
    # Build context-aware example
    if parents:
        parent = parents[0]
        if parent == "rule":
            example_lines.append(f"<rule>")
            example_lines.append(f"  <description>Example rule using {tag_name}</description>")
            example_lines.append(f"  <{tag_name}/>")
            example_lines.append(f"</rule>")
        elif parent == "actions":
            example_lines.append(f"<rule>")
            example_lines.append(f"  <conditions>")
            example_lines.append(f"    <and/>")
            example_lines.append(f"  </conditions>")
            example_lines.append(f"  <actions>")
            example_lines.append(f"    <{tag_name}/>")
            example_lines.append(f"  </actions>")
            example_lines.append(f"</rule>")
        elif parent == "conditions":
            example_lines.append(f"<rule>")
            example_lines.append(f"  <conditions>")
            example_lines.append(f"    <{tag_name}/>")
            example_lines.append(f"  </conditions>")
            example_lines.append(f"  <actions/>")
            example_lines.append(f"</rule>")
        elif parent in {"and", "or"}:
            example_lines.append(f"<rule>")
            example_lines.append(f"  <conditions>")
            example_lines.append(f"    <and>")
            example_lines.append(f"      <{tag_name}/>")
            example_lines.append(f"    </and>")
            example_lines.append(f"  </conditions>")
            example_lines.append(f"</rule>")
        else:
            example_lines.append(f"<{parent}>")
            if children:
                child_key = list(children.keys())[0]
                example_lines.append(f"  <{tag_name}>")
                example_lines.append(f"    <{child_key}/>")
                example_lines.append(f"  </{tag_name}>")
            else:
                example_lines.append(f"  <{tag_name}/>")
            example_lines.append(f"</{parent}>")
    else:
        # No parent info - show standalone
        if children:
            child_keys = list(children.keys())[:3]
            example_lines.append(f"<{tag_name}>")
            for child in child_keys:
                example_lines.append(f"  <{child}/>")
            example_lines.append(f"</{tag_name}>")
        else:
            example_lines.append(f"<{tag_name}/>")
    
    example_lines.append("")
    example_lines.append(f"Use case: {description[:100] if description else 'Define policy logic'}")
    
    return {
        "instruction": instruction,
        "output": "\n".join(example_lines),
    }


def build_tasks_for_tag(tag_name: str, payload: Dict) -> List[Dict[str, str]]:
    """Build comprehensive training records for a single DTD tag."""
    tasks = []
    
    # 1. Tag definition - what it is and its metadata
    tasks.append(make_tag_definition_record(tag_name, payload))
    
    # 2. Attributes - what parameters it accepts
    tasks.append(make_attribute_record(tag_name, payload))
    
    # 3. When to use - scenario-based learning
    tasks.append(make_when_to_use_record(tag_name, payload))
    
    # 4. Valid combinations - hierarchical learning
    tasks.append(make_valid_combination_record(tag_name, payload))
    
    # 5. Error detection - learn from mistakes
    tasks.append(make_error_detection_record(tag_name, payload))
    
    # 6. Q&A - direct comprehension
    tasks.append(make_qa_record(tag_name, payload))
    
    # 7. Examples - practical usage patterns
    tasks.append(make_example_record(tag_name, payload))
    
    return tasks


def generate_dataset(input_file: str, output_file: str) -> Tuple[int, int]:
    data = load_json_file(input_file)
    tags = select_tag_entries(data)

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    record_count = 0
    with open(output_file, "w", encoding="utf-8") as outfile:
        for tag_name, payload in tags:
            tasks = build_tasks_for_tag(tag_name, payload)
            for task in tasks:
                outfile.write(json.dumps(task, ensure_ascii=False) + "\n")
                record_count += 1

    return len(tags), record_count


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate train.jsonl style data from unified_dtd_data.json"
    )
    parser.add_argument(
        "--input",
        default=DEFAULT_INPUT_FILE,
        help="Path to unified_dtd_data.json",
    )
    parser.add_argument(
        "--output",
        default=DEFAULT_OUTPUT_FILE,
        help="Path to output training JSONL file",
    )
    parser.add_argument(
        "--log",
        default=DEFAULT_LOG_FILE,
        help="Path to log file",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    configure_logger(args.log)

    logging.info("Starting DTD training data generation pipeline")
    logging.info(f"Input file: {args.input}")
    logging.info(f"Output file: {args.output}")

    if not os.path.exists(args.input):
        raise FileNotFoundError(f"Input file not found: {args.input}")

    tag_count, record_count = generate_dataset(args.input, args.output)
    logging.info(f"Generated records for {tag_count} tags")
    logging.info(f"Total JSONL rows written: {record_count}")
    logging.info("DTD training data generation pipeline completed")


if __name__ == "__main__":
    main()