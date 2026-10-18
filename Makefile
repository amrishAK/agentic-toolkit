.DEFAULT_GOAL := help

ifeq ($(OS),Windows_NT)
PYTHON ?= python
else
PYTHON ?= python3
endif

CLIENT ?= copilot
SCOPE ?= user
SUITE ?= engineering
AGENT ?=
SKILL ?=
SKILLS ?=
LANGUAGE_SKILLS ?= include
WORKSPACE ?=
DESTDIR ?=

export CLIENT SCOPE SUITE AGENT SKILL SKILLS LANGUAGE_SKILLS WORKSPACE DESTDIR

.PHONY: help list plan install check

help:
	@"$(PYTHON)" -B -m scripts.install help

list:
	@"$(PYTHON)" -B -m scripts.install list

plan:
	@"$(PYTHON)" -B -m scripts.install plan

install:
	@"$(PYTHON)" -B -m scripts.install install

check:
	@"$(PYTHON)" -B -m unittest discover -s tests -v
