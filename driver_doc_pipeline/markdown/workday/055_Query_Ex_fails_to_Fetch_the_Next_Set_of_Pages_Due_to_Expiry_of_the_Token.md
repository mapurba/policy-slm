# 9.12 Query-Ex fails to Fetch the Next Set of Pages Due to Expiry of the Token

Workaround: The recommended Query-Ex timeout option must be set to either 120 or more. If you specify a value less than 120, the token for Query-Ex might expire.
