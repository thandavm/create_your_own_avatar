import streamlit as st
import json
import boto3
import numpy as np
from matplotlib import pyplot as plt

#Enter the information per your account
access_key = ''
secret_key = ''
region = 'us-east-1'
model_end_point = ''

sagemaker_runtime_client = boto3.client('runtime.sagemaker',
                            aws_access_key_id= access_key,
                            aws_secret_access_key=secret_key,
                            region_name=region)

st.subheader('Test your fine tuned LLM - Text to Image')

input_value = st.text_area('Input for Stable Diffusion: ', placeholder='Ask me anything ...', key='prompt', height =  250, max_chars= 5000)
submit_button = st.button("Generate")

if submit_button:
    response = sagemaker_runtime_client.invoke_endpoint(EndpointName=model_end_point, 
                        Body=input_value, 
                        ContentType='application/x-text')
    
    response_body = json.loads(response['Body'].read().decode())
    generated_image = response_body['generated_image']
    plt.figure(figsize=(12, 12))
    st.image(np.array(generated_image))