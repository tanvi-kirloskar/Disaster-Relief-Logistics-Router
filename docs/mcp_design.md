# MCP Inventory System Design

## Purpose

The Model Context Protocol (MCP) component provides external resource information to agents.

The Resource Planner Agent uses MCP to retrieve available inventory and make allocation decisions.

This demonstrates tool usage and external context integration within a multi-agent workflow.

---

## Inventory Resource

The inventory is stored in:

data/inventory.json

Example:

```json
{
  "boats": 5,
  "ambulances": 2,
  "medical_kits": 20,
  "food_kits": 100,
  "shelter_beds": 40
}
```

---

## MCP Architecture

Citizen Report

↓

Resource Planner Agent

↓

MCP Server

↓

Inventory Tool

↓

Inventory Data

↓

Resource Recommendation

---

## MCP Tools

### Tool 1: get_inventory()

Purpose:

Retrieve current inventory.

Input:

None

Output:

```json
{
  "boats": 5,
  "ambulances": 2,
  "medical_kits": 20,
  "food_kits": 100,
  "shelter_beds": 40
}
```

Used by:

* Resource Planner Agent

---

### Tool 2: allocate_resources()

Purpose:

Update inventory after resource allocation.

Input:

```json
{
  "boats": 1,
  "food_kits": 10
}
```

Output:

Updated inventory.

Used by:

* Resource Planner Agent

---

## Agent Interaction Example

Incident:

"12 people trapped on rooftop during flood."

Severity:

HIGH

Inventory Retrieved:

* Boats: 5
* Food Kits: 100

Agent Recommendation:

* Allocate 1 Rescue Boat
* Allocate 10 Food Kits

Inventory Updated:

* Boats: 4
* Food Kits: 90

---

## Why MCP Was Chosen

The Google AI Agents Intensive emphasized external tool integration through MCP.

This project uses MCP to:

* Demonstrate tool use
* Separate reasoning from data access
* Simulate real-world resource management systems

Although simplified, the MCP inventory server reflects the same architectural pattern used in production agent systems.

```
```
