import erniebot

class MainframeAgents:
    def __init__(self, ernie_api_key):
        erniebot.api_type = "aistudio"
        erniebot.access_token = ernie_api_key
        
    def process_jcl(self, jcl_text):
        # Agent 1: Parser
        parsed_response = erniebot.ChatCompletion.create(
            model="ernie-4.0",
            messages=[{
                "role": "user",
                "content": f"You are a JCL Parser. Extract job name, step names, programs (PGM=), datasets (DD), and errors from:\n\n{jcl_text}"
            }]
        )
        parsed = parsed_response.get_result()
        
        # Agent 2: Analyzer
        analysis_response = erniebot.ChatCompletion.create(
            model="ernie-4.0",
            messages=[{
                "role": "user",
                "content": f"You are an error analyzer. Analyze this parsed JCL and identify issues:\n\n{parsed}"
            }]
        )
        analysis = analysis_response.get_result()
        
        # Agent 3: Commander
        commands_response = erniebot.ChatCompletion.create(
            model="ernie-4.0",
            messages=[{
                "role": "user",
                "content": f"You are a Zowe CLI expert. Generate exact Zowe commands to fix:\n\n{analysis}"
            }]
        )
        commands = commands_response.get_result()
        
        return {
            "parsed": parsed,
            "analysis": analysis,
            "commands": commands
        }
