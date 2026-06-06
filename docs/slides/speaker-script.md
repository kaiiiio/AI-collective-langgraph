# Speaker Script: LangGraph and LangSmith Reliable AI Workflows

Use this as your talk track. The visible slides stay audience-facing; this file is for what you say out loud.

## Slide 1: Reliable AI Workflows

Say: Today we are not learning LangGraph as a random library. We are learning how to make AI workflows reliable. A reliable AI system is not just a model call. It has state, steps, routes, retries, review, and traces.

Ask: Think of one AI output you have seen that was hard to debug. What made it hard?

## Slide 2: The Real Problem

Say: Calling the model is usually the easiest part. The hard part is everything around it: loading data, writing the prompt, parsing output, checking structure, retrying failure, saving results, and debugging what happened.

Ask: If the model gives bad JSON, should that be hidden inside one big function, or should the workflow show that failure?

## Slide 3: Two Real Projects

Say: We will use two real workflow shapes. First, content generation at scale. Second, a regulated licensing workflow. They look different, but the architecture problem is the same: move state through controlled steps.

Ask: What do both projects need before they can be trusted?

## Slide 4: LangGraph Mental Model

Say: This is the entire idea. State enters a node. The node does one bounded job. The node returns an update. The graph merges that update into state and moves to the next node.

Ask: After a node runs, what is the one question we should always ask? Answer: what changed in state?

## Slide 5: Full Minimal Code

Say: Here is a complete LangGraph program. Notice the imports, the state type, the node function, the edges, compile, and invoke. The node does not return the whole state. It returns only the new `response` field.

Ask: What did `answer_node` receive, and what did it return?

## Slide 6: Multi-Node Code

Say: A bigger graph is still just connected functions. `fetch_context` creates context. `build_prompt` uses that context. `call_model` uses the prompt. Each step depends on state created by the step before it.

Ask: What would break if `build_prompt` ran before `fetch_context`?

## Slide 7: Project 1 Flow

Say: Content generation is already a workflow. You load company data, build a prompt, call a model, parse JSON, repair failure, validate schema, save content, and update progress.

Ask: Which step should own retry behavior: the model call, the parser, or the graph route?

## Slide 8: Content State

Say: This state object is the contract for one content-generation run. It holds the input ids, context, prompt, raw AI response, parsed content, validation errors, retry count, and final content.

Ask: Which fields exist before the AI call? Which fields exist after it?

## Slide 9: Content Nodes

Say: Each service step becomes a named node. This matters because the workflow becomes readable. Instead of one hidden function, we can inspect `load_context`, `build_prompt`, `call_ai_provider`, and `parse_json`.

Ask: What does each node add to state?

## Slide 10: Parse JSON Node

Say: This node handles a real AI failure: broken JSON. If parsing works, it writes `parsed_content`. If parsing fails, it writes `validation_errors`. The failure becomes data the graph can route on.

Ask: Why is returning `validation_errors` better than just printing the error?

## Slide 11: Conditional Retry Code

Say: A conditional edge is just a Python function that looks at state and returns a route name. If there are errors and retries are still available, repair. If retries are exhausted, fail. If there are no errors, continue.

Ask: What route happens when `validation_errors` exists and `retry_count` is already 2?

## Slide 12: Content Graph Code

Say: This slide registers the content workflow nodes. The names matter because these become the readable structure of the workflow and the trace.

Ask: Which node is responsible for raw model output, and which node is responsible for interpreting it?

## Slide 13: Content Conditional Edges

Say: Now the graph becomes robust. Valid output goes to schema enforcement and save. Invalid output loops to repair and model retry. Repeated invalid output exits through `mark_failed`.

Ask: Trace one broken JSON run from `parse_json` to the end.

## Slide 14: Why LangGraph Helps Project 1

Say: LangGraph makes content generation controllable. Retries are visible, schema gates protect saved content, and bulk jobs can report success or failure per page.

Ask: If you generated 500 pages, which of these benefits would matter first?

## Slide 15: Project 2 Flow

Say: Licensing is not one prompt. It is a sequence of evidence, classification, policy generation, mapping, gap analysis, review, export, and remediation.

Ask: Which steps should never proceed without evidence?

## Slide 16: Licensing State

Say: This state object separates profile data, uploaded documents, indexed chunks, classifications, policies, mappings, gaps, human decisions, and export output.

Ask: Which fields are facts? Which fields are AI analysis? Which fields are human decisions?

## Slide 17: Licensing Nodes

Say: Classification, mapping, and gap analysis are separate because they carry different risk. Keeping them separate makes each output reviewable.

Ask: Why would one giant prompt be harder to audit?

## Slide 18: Evidence Route Code

Say: This route is the safety gate. If classification has enough evidence and confidence, the graph continues. If not, it routes to human review.

Ask: What two state values control this route?

## Slide 19: Human Review Code

Say: Human review is part of the graph, not outside it. The node identifies high-risk gaps and records whether review is required.

Ask: How does this help if someone audits the case later?

## Slide 20: Licensing Graph Code

Say: The graph starts with intake validation and document indexing before classification. That order matters because classification should be based on prepared evidence.

Ask: What would happen if classification ran before documents were indexed?

## Slide 21: Licensing Conditional Edges

Say: Approval gates are routes. Strong evidence enters the policy/mapping/gap path. Weak evidence goes to human review. The graph protects downstream work.

Ask: Trace the low-confidence path.

## Slide 22: Why LangGraph Helps Project 2

Say: In regulated AI, structure is not optional. Evidence gates, auditability, and human control are what make the workflow defensible.

Ask: Which of these would you require before trusting the system in production?

## Slide 23: LangSmith Mental Model

Say: LangGraph controls the path. LangSmith shows what happened. A trace is a timeline of one run, including node runs, model calls, tool calls, outputs, errors, latency, and cost.

Ask: After a bad output, which node would you inspect first?

## Slide 24: LangSmith Tracing Code

Say: `@traceable` gives important functions readable trace names. This does not change the business logic. It makes the run visible in LangSmith.

Ask: What trace name would you use for the JSON repair step?

## Slide 25: LangSmith Setup

Say: Tracing is configured through environment variables. Docker Compose passes `.env` values into the container. The key point: never hardcode API keys in graph code.

Ask: Why is `.env` safer than putting the key in a Python file?

## Slide 26: LangSmith Debugging

Say: LangSmith is useful because it answers concrete questions: which prompt caused broken JSON, which locations failed, which provider was slow, which evidence supported classification, and which node created the gap.

Ask: Which question would you ask first during a production failure?

## Slide 27: LangSmith Evaluations

Say: Evaluations turn quality into repeatable checks. Instead of saying “this output looks good,” we check JSON validity, schema match, local relevance, fake claims, and citations.

Ask: What evaluation would you add for the licensing workflow?

## Slide 28: Production Monitoring

Say: After deployment, LangSmith helps track failure rate, retry count, latency, cost, and bad examples. Bad examples should become future evaluation data.

Ask: Which metric would tell you the workflow is getting worse?

## Slide 29: Honest Framing

Say: We are using real project flows as examples of what LangGraph can formalize. Be precise: do not claim an existing system uses LangGraph unless it actually does.

Ask: Why does honest framing matter in technical demos?

## Slide 30: Closing

Say: The final lesson is simple: reliable AI is controlled workflow. The model matters, but the system around the model is what makes it inspectable, retryable, reviewable, and improvable.

Ask: Summarize LangGraph in one sentence. Then summarize LangSmith in one sentence.
