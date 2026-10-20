.DEFAULT_GOAL := help

ifeq ($(OS),Windows_NT)
PYTHON ?= python
else
PYTHON ?= python3
endif

CLIENT ?= copilot
SCOPE ?= user
SUITE ?= software-product-development
PACKAGE ?=
AGENT ?=
SKILL ?=
SKILLS ?=
LANGUAGE_SKILLS ?= include
OPTIONAL_PACKAGES ?= include
WORKSPACE ?=
DESTDIR ?=

export CLIENT SCOPE SUITE PACKAGE AGENT SKILL SKILLS LANGUAGE_SKILLS OPTIONAL_PACKAGES WORKSPACE DESTDIR

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
	@"$(PYTHON)" -B -m scripts.validate_manifests
	@"$(PYTHON)" -B -m unittest discover -s tests -v
