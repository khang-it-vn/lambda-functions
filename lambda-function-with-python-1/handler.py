import json
import traceback


def hello(event, context):
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!"
    }
    
import json

def get_info(event, context):
    try:
        # In ra từng thuộc tính của context để biết thông tin chi tiết
        print("Function Name:", context.function_name)
        print("Function Version:", context.function_version)
        print("Invoked Function ARN:", context.invoked_function_arn)
        print("Memory Limit (MB):", context.memory_limit_in_mb)
        print("AWS Request ID:", context.aws_request_id)
        print("Log Group Name:", context.log_group_name)
        print("Log Stream Name:", context.log_stream_name)
        # Thêm các thuộc tính khác nếu cần

        # Chuyển đổi context thành một từ điển có thể chuyển đổi sang JSON
        context_dict = {
            "function_name": context.function_name,
            "function_version": context.function_version,
            "invoked_function_arn": context.invoked_function_arn,
            "memory_limit_mb": context.memory_limit_in_mb,
            "aws_request_id": context.aws_request_id,
            "log_group_name": context.log_group_name,
            "log_stream_name": context.log_stream_name 
        }

        # Chuyển đổi từ điển thành chuỗi JSON
        json_dump_context = json.dumps(context_dict)
        print("Context", json_dump_context)
        
        json_dump_event =  json.dumps(event)
        print("Event", json_dump_event)
        
        
        body = json.loads(event["body"])
        print("HTTP METHOD RECEIVED: ",body)
        # Handle GET request
        
        response = {
            "statusCode": 200,
            "context": context_dict,
            "event": event,
            "body": json.dumps(body)
        }
        
        print("Response: ", response)
        return response 
    except Exception as e:
        traceback.print_exc()
        return {
                "statusCode": 400,
                "responseMessage": "System error"
            }
