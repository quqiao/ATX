#!/usr/bin/env python
# coding=utf-8



from time import sleep, strftime
import public.methods as public
from public import logutils
log = logutils.getLogger(__name__)

class Channel(public.Methods):
    def login(self, driver):
        driver.click(1316,840)
        
