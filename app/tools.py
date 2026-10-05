from fastmcp import Context
from mcp import CreateMessageRequest, CreateMessageResult, SamplingMessage
from mcp_types import CreateMessageRequestParams, InputRequiredResult, TextContent

from app.server import mcp


@mcp.tool
def echo(s: str) -> str:
    """Echo the provided string"""
    return s


# Demo of sampling using the guard pattern
# Note: eventhough "sampling" is not in the spec anymore,
# you can still implement the same idea in user-land
# @see https://gofastmcp.com/servers/sampling
@mcp.tool
async def to_sql(dialect: str, intent: str, ctx: Context) -> str | InputRequiredResult:
    """
    Generate a proper SQL query depending on the provided dialect
    """
    responses = ctx.input_responses
    if responses is None:
        # First step: we analyze the requested dialect and generate a complete prompt
        if (dialect == "sqlite"):
            full_prompt = f"""
User want's to generate sqlite SQL queries.
Keep in mind that sqlite works in memory.
Generate the requested query, for the following user intent: {intent}
"""
        else:
            full_prompt = f"""
User want's to generate a SQL query using dialect {dialect}.
Generate the requested query, for the following user intent: {intent}
"""
        return InputRequiredResult(
            result_type="input_required",
            input_requests={
                "answer": CreateMessageRequest(
                    method="sampling/createMessage",
                    params=CreateMessageRequestParams(
                        messages=[
                            SamplingMessage(
                                role="user",
                                content=TextContent(
                                    type="text", text=full_prompt),
                            )
                        ],
                        max_tokens=100,
                    ),
                )
            },
        )
    # Step 2: the tool was called again, this time with the LLM's answer
    answer = responses["answer"]
    if isinstance(answer, CreateMessageResult) and isinstance(
        answer.content, TextContent
    ):
        # Here we could validate the generated SQL for instance,
        # using a static analyzer
        return answer.content.text
    # Scenario where the LLM refused to answer
    return "The client returned no completion. We can't create a SQL query without the host's LLM help!"
