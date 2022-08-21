#!/usr/bin/env bash

find test/automated -name '*.py' -print0 | xargs -0 pytest