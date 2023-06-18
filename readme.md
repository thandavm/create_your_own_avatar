# Make your own avatar using SageMaker Foundation Model Hub

## Pre-requisites

1. AWS Account
2. Acess to Foundation Model hub within the AWS Account - If you do not have access request access as per the guidelines provided in <https://wiki.amazon.com/bin/view/SageMaker-JumpStart/FoundationModels>
3. SageMaker Domain, User and IAM role with full access to SageMaker and Amazon S3
4. Create a user with admin previliges and capture the access key and secret key securely
5. Use us-east-1 for your lab

## Create the data set

1. Create a json file simialar to the below and name it dataset_info.json
![Alt text](image.png)
2. Upload the images and the json file on to an Amazon S3 bucket
![Alt text](image-1.png)

## Fine tune Stable Diffusion Model

1. Log in to your SageMaker Studio
2. Click on SageMaker Jumpstarts -> Models, Notebooks and solutions
3. Search for Stable Diffusion and select "Stable Diffusion 2.1 base"
![Alt text](image-2.png)
4. Click on the "Train" tab
5. For the training dataset, select the Amazon S3 prefix where you uploaded your data
![Alt text](image-3.png)

6. Click on "Train"

This will start the fine tuning of the Stable diffusion model and will take ~10 - 12 mins to fine tune

## Deploy the fine tuned Model

1. Once fine tuning is complete, click on the "Deploy" tab
2. Enter a name for the fine tuned model,  keep the rest the same
![Alt text](image-4.png)
3. Click on "Deploy".  this will take ~7 -8 minutes to complete

## Play with the model and create your own avatars

1. Clone the repo
```git clone```
2. Install the required sdk
```pip install -r requirements.txt```
3. Open the app.py and add your access key, secret key and model end point name
4. run the app
```streamlit run app.py```
5. Unleash your imagination in the text area.  Few sample below
 "meena man as 10 year old boy"
