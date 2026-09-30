from fastmcp import Context
from mcp import CreateMessageRequest, CreateMessageResult, SamplingMessage
from mcp_types import CreateMessageRequestParams, InputRequiredResult, TextContent

from app.server import mcp


@mcp.tool
def echo(s: str) -> str:
    """Echo the provided string"""
    return s


# Sampling: a tool asks a question to the host's LLM
@mcp.tool
async def create_poem(theme: str, ctx: Context) -> str | InputRequiredResult:
    """
    Create a poem. This tool will prompt the LLM with additional context to generate a good poem.
    """
    responses = ctx.input_responses
    if responses is None:
        # First step: we analyze the user's poeme theme and create a refined prompt
        full_prompt = f"""
User requested a poem on the theme: {theme}.
Generate 3 verses in prose.
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
        return answer.content.text
    # Scenario where the LLM refused to answer
    return "The client returned no completion. We can't create a poem without the host's LLM help!"
