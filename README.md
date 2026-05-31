# Task execution by Code Generation Results

This repository contains evaluation results for multiple open-source coding language models on a suite of **322 real-world file system and automation tasks**.

## Benchmark Setup

Each model is evaluated using an execution-driven loop in which the model must solve tasks by generating Python or shell code.

The model receives:

* A system prompt defining the execution environment
* A single high-level task description

The model can only interact with the environment by writing executable code. After each execution it receives:

* Standard output (stdout)
* Standard error (stderr)
* Exit code

The model must reason from execution results and iteratively improve its solution until the task is completed.

No internet access, browser access, external tools, or agent frameworks are available during evaluation.

## System Prompt Summary

Models are instructed to:

* Solve tasks through Python or shell code
* Learn from execution traces
* Take one step at a time
* Avoid explanations and natural-language reasoning
* Produce only executable code at each iteration
* Make measurable progress toward task completion

This setup evaluates a model's ability to perform autonomous execution-guided reasoning rather than single-shot code generation.

## Task Suite

The benchmark consists of **322 tasks** covering practical filesystem operations, data processing, reporting, search, analysis, and automation workflows.

Example tasks include:

* Finding the largest files in a directory tree
* Counting lines across source files
* Detecting duplicate filenames
* Computing file hashes
* Generating CSV reports
* Discovering broken symbolic links
* Identifying recently modified files
* Analyzing file extensions and directory structures

## Repository Structure

| Directory                              | Model                                              |
| -------------------------------------- | -------------------------------------------------- |
| `Res_CodeGemma-7B-IT`                  | CodeGemma 7B IT                                    |
| `Res_Qwen2.5-Coder-7B-Instruct`        | Qwen2.5-Coder 7B Instruct                          |
| `Res_round2_Qwen2.5-Coder-7B-Instruct` | Second evaluation run of Qwen2.5-Coder 7B Instruct |
| `Res_Qwen2.5-Coder-32B-Instruct`       | Qwen2.5-Coder 32B Instruct                         |

Each result directory contains:

* Generated code for every step
* Execution traces
* Standard output logs
* Standard error logs
* Return codes
* Conversation history snapshots
* Per-step JSON logs

## Execution Framework

For every task:

1. A task description is selected.
2. The model generates Python or shell code.
3. The code is executed in a real environment.
4. Execution traces are returned to the model.
5. The model generates the next step.
6. All artifacts are saved for analysis.

This process continues until the task is terminated or completed.

## Purpose

The goal of this benchmark is to study:

* Autonomous coding capability
* Execution-guided reasoning
* Multi-step problem solving
* Error recovery and debugging
* Tool-free agentic behavior
* Comparative performance of open-source coding models

The repository preserves raw outputs and execution traces to support reproducibility and independent analysis.
