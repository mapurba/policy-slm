# 9.4 Workday Driver Displays an Error Message While Shutting Down

Workday driver displays the following error message if a shutdown command is executed during the polling time or during the migration process when the cache update is in progress.

```
<output>
                <status
level="error">com.netiq.dirxml.driver.workday.exception.PollException: Error
encountered while polling JobProfile
        at
com.netiq.dirxml.driver.workday.WDPublisherHandler.pollJobProfile(WDPublisherHandler.java:533)
        at
com.netiq.dirxml.driver.workday.WDPublisherHandler.doPoll(WDPublisherHandler.java:256)
        at
com.netiq.dirxml.driver.workday.WDPublisherShim.doPoll(WDPublisherShim.java:140)
        at
com.netiq.dirxml.driver.workday.WDPublisherShim.start(WDPublisherShim.java:116)
        at com.novell.nds.dirxml.remote.loader.Driver.run(Driver.java:899)
        at java.lang.Thread.run(Thread.java:748)
Caused by: com.netiq.dirxml.driver.workday.exception.CacheException: Cache
shutdown in progress...
        at
com.netiq.dirxml.driver.workday.cache.MapDbCache.checkShutdown(MapDbCache.java:250)
        at
com.netiq.dirxml.driver.workday.cache.CacheManager.openJobProfileCacheFiles(CacheManager.java:735)
        at
com.netiq.dirxml.driver.workday.WDPublisherHandler.pollJobProfile(WDPublisherHandler.java:505)
        ... 5 more
</status>
        </output>
```

There is no workaround at this moment but you can ignore the error message and wait for the driver to shut down.
