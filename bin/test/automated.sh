#!/usr/bin/env bash

find test -name '*.py' -print0 | xargs -0 pytest