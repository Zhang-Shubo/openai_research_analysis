import os
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key="40807e176ac44461b3080a6476d10fa1",  
    api_version="2023-12-01-preview",
    azure_endpoint = "https://instance-nlp-story-local-3.openai.azure.com/"
)
# client = AzureOpenAI(
#     # https://learn.microsoft.com/en-us/azure/ai-services/openai/reference#rest-api-versioning
#     api_version="2023-12-01-preview",
#     api_key=os.environ["AZURE_OPENAI_API_KEY"],
#     # https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/create-resource?pivots=web-portal#create-a-resource
#     azure_endpoint = "https://instance-nlp-story-local-3.openai.azure.com/",
# )


def request_openai(message):
    result = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[{"role": "system", "content": message}],
        temperature=0.0
    )
    analysis = result.dict()["choices"][0]["message"]["content"]
    print({"analysis": analysis})
    return analysis


if __name__ == "__main__":
    print(request_openai("hello"))