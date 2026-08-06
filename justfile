# Desktop-App-Template Task Automation — Root Justfile
# https://github.com/casey/just

set shell := ["bash", "-c"]
set unstable := true

# --- Sub-module declarations (imported from tools/) ---

mod tool_helper     "tools/helper/justfile"
mod tool_dev        "tools/dev/justfile"
mod tool_build      "tools/build/justfile"
mod tool_test       "tools/test/justfile"
mod tool_validation "tools/validation/justfile"
mod tool_docs       "tools/docs/justfile"
mod tool_bench      "tools/bench/justfile"
mod tool_ci         "tools/ci/justfile"

# --- Default target ---

default: help

# List all commands across every sub-module
help:
    @just tool_helper::help

# --- Setup & maintenance (→ tools/dev) ---

setup:
    @just tool_dev::setup

update:
    @just tool_dev::update

pre-commit:
    @just tool_dev::pre-commit

clean:
    @just tool_dev::clean

# --- Build (→ tools/build) ---

build:
    @just tool_build::all

# --- Test (→ tools/test) ---

test:
    @just tool_test::all

# --- Validation (→ tools/validation) ---

lint:
    @just tool_validation::all

# --- Docs (→ tools/docs) ---

docs:
    @just tool_docs::build

# --- Benchmark (→ tools/bench) ---

bench:
    @just tool_bench::all

# --- Docker (→ tools/dev) ---

docker-up:
    docker compose -f infra/docker/docker-compose.yml up --build

docker-down:
    docker compose -f infra/docker/docker-compose.yml down
