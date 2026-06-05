param(
    [Parameter(Position = 0)]
    [string]$Command = "help",

    [Parameter(Position = 1)]
    [string]$Module
)

$ErrorActionPreference = "Stop"

function Show-Help {
    @"
LangGraph Learning Lab

Usage:
  .\lab.ps1 build
  .\lab.ps1 list
  .\lab.ps1 module 1
  .\lab.ps1 1
  .\lab.ps1 capstone
  .\lab.ps1 test
  .\lab.ps1 ruff
  .\lab.ps1 mypy
  .\lab.ps1 down
"@
}

function Get-ModulePath {
    param([string]$Number)

    switch ($Number) {
        "1" { "modules/01_hello_graph/main.py" }
        "2" { "modules/02_state_management/main.py" }
        "3" { "modules/03_conditional_edges/main.py" }
        "4" { "modules/04_tools/main.py" }
        "5" { "modules/05_memory/main.py" }
        "6" { "modules/06_agent/main.py" }
        "7" { "modules/07_multi_agent/main.py" }
        "8" { "modules/08_human_review/main.py" }
        "9" { "modules/09_langsmith/main.py" }
        "10" { "modules/10_capstone_project/main.py" }
        default {
            Write-Error "Unknown module: $Number"
        }
    }
}

function Show-Modules {
    @"
1  01_hello_graph         Graph, node, edge, execution flow
2  02_state_management    Typed state before and after execution
3  03_conditional_edges   Routing to joke or fact branch
4  04_tools               Calculator, weather mock, stock mock
5  05_memory              Conversation memory
6  06_agent               Tool selection and answer flow
7  07_multi_agent         Research, writer, reviewer agents
8  08_human_review        Approval before publish
9  09_langsmith           Tracing and observability
10 10_capstone_project    AI research assistant
"@
}

switch ($Command.ToLowerInvariant()) {
    { $_ -in @("help", "-h", "--help") } {
        Show-Help
    }
    "build" {
        docker compose build
    }
    "list" {
        Show-Modules
    }
    "module" {
        if (-not $Module) {
            Write-Error "Usage: .\lab.ps1 module <1-10>"
        }
        docker compose run --rm lab python (Get-ModulePath $Module)
    }
    { $_ -match "^(?:[1-9]|10)$" } {
        docker compose run --rm lab python (Get-ModulePath $Command)
    }
    "capstone" {
        docker compose run --rm lab python (Get-ModulePath "10")
    }
    "test" {
        docker compose run --rm test
    }
    "ruff" {
        docker compose run --rm lab ruff check .
    }
    "mypy" {
        docker compose run --rm lab mypy app
    }
    "down" {
        docker compose down
    }
    default {
        Write-Error "Unknown command: $Command"
    }
}
