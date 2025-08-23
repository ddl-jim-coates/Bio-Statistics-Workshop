# Biostatistics Workshop - Step D Train and Evaluate
#### [Made by Jim Coates with Scribe](https://scribehow.com/shared/Biostatistics_Workshop_-_Step_D_Train_and_Evaluate__g0rnnR8ASCa06azGdAshrQ)


Alert: Alert! In order to use our new snapshot from Step C we need to either restart our workspace or create a new one so that it can be mounted.


1\. From the "Workspace" screen click "Settings"

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-23/8ab0e20c-6600-45b2-b471-b3c25fd06ab6/ascreenshot.jpeg?tl_px=63,0&br_px=1440,769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=762,235)


2\. Click "Save & Restart"

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-23/b3bb2c1b-a730-41b8-8360-4bcf83545650/ascreenshot.jpeg?tl_px=63,128&br_px=1440,898&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=725,546)


3\. Navigate to `exercises/d_TrainingAndEvaluation/workflow.py` and review the file

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-23/1c38cd53-b3ab-4282-bbd6-8708125e3b70/ascreenshot.jpeg?tl_px=0,128&br_px=1376,898&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=443,370)


4\. Click "File" -&gt; "New "-&gt; "Terminal"

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-23/406dba0c-8a1c-46fa-b641-ba3c341bbfca/ascreenshot.jpeg?tl_px=0,0&br_px=1376,769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=427,169)


5\. Execute the flow command [[pyflyte run --remote exercises/d_TrainingAndEvaluation/workflow.py clinical_trial_adverse_event_prediction_workflow]]

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-23/82ad8df0-f22f-45b1-a584-83d21b4eaed7/ascreenshot.jpeg?tl_px=0,0&br_px=1440,804&force_format=jpeg&q=100&width=1120.0)


6\. Navigate back to the Domino Tab and then Click "Flows"

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-23/153bfb03-e6bf-4427-9b76-9ee51a3956cf/user_cropped_screenshot.webp?tl_px=0,0&br_px=1376,769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=93,-11)


7\. Click the workflow name

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-23/ca8c25f8-f67c-4868-a095-06eb9eae114e/user_cropped_screenshot.webp?tl_px=0,0&br_px=2874,1450&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=313,155)


8\. Click the active run

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-23/ecb976aa-d750-4ee0-9f67-35029eba5855/user_cropped_screenshot.webp?tl_px=0,0&br_px=2870,1464&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=209,217)


9\. Select the graph view to inspect the training flow progress

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-23/cb0c3757-02d7-4be6-9378-d1bbfed0ae14/ascreenshot.jpeg?tl_px=0,0&br_px=1376,769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=255,207)


10\. Once completed - select nodes to view results

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-23/b35d4d09-67d4-422a-82af-5410f35acf63/ascreenshot.jpeg?tl_px=39,104&br_px=1416,873&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=524,277)


11\. Details are an encapsulation of all the reproducible elements of our flow

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-23/0e48f38a-f613-4a83-8b57-9541fe48ce59/screenshot.webp?tl_px=0,0&br_px=2846,1462&force_format=jpeg&q=100&width=1120.0)


12\. Click Experiments to view experiments logged from our flow

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-23/274d8a34-07ff-455c-ba15-d411be230ffe/user_cropped_screenshot.webp?tl_px=0,0&br_px=2846,1462&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=17,297)


13\. Click Clinical Trial AE Prediction

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-23/0fae35ce-331b-42ec-a141-d1da1e8e54a3/ascreenshot.jpeg?tl_px=0,0&br_px=1376,769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=326,229)


14\. Select all 3 models then click the "Compare" icon

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-23/09474bce-da3a-4fd1-ab9c-6074e46f2a9b/user_cropped_screenshot.webp?tl_px=0,0&br_px=2786,1354&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=216,266)


15\. Compare model performances and select XGBoost

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-23/c708c3c1-5e26-45a0-8cb1-25bdfe4a626c/user_cropped_screenshot.webp?tl_px=0,0&br_px=2828,1424&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=302,383)


16\. Click "Register model from run"

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-23/843290e1-969c-471a-9acc-6d339c8e2528/ascreenshot.jpeg?tl_px=63,0&br_px=1440,769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=910,138)


17\. Name your model XGBoost, select the "Logged MLflow Model" and give it a descrption

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-23/27a10477-3f61-4a0a-a156-7e79c0349ce7/ascreenshot.jpeg?tl_px=0,128&br_px=1376,898&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=421,289)


18\. Click "Register Model"

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-23/847f4004-4f2e-4e8c-a6f6-b0e55f7899e6/ascreenshot.jpeg?tl_px=63,128&br_px=1440,898&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=615,546)


19\. Click the link to inspect your newly registered model

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-23/27e4120b-57a3-4e0c-92ac-03d4338e56cb/ascreenshot.jpeg?tl_px=0,128&br_px=1376,898&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=335,281)


20\. From the model card select "Endpoints"

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-23/6c267a6f-6a34-4801-bcf0-e4c94846f8a9/user_cropped_screenshot.webp?tl_px=0,0&br_px=2765,1452&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=274,102)


21\. Click "Create Domino endpoint"

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-23/56e4e6ac-588a-45a0-abda-fb4eaf54ba86/ascreenshot.jpeg?tl_px=63,128&br_px=1440,898&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=554,302)


22\. Name your endpoint and click Next

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-23/dcb451b2-872b-4acd-900e-4836ed082a19/ascreenshot.jpeg?tl_px=0,4&br_px=1376,773&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=164,276)


23\. Click "Choose from model registry"

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-23/849eace7-bb58-4524-b7a9-c5d6e1e81881/ascreenshot.jpeg?tl_px=0,12&br_px=1376,781&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=29,276)


24\. Select our XGBoost Model

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-23/f2cbe604-8ee4-4ba3-8bea-a148fad07fc4/ascreenshot.jpeg?tl_px=0,128&br_px=1376,898&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=197,298)


25\. Click "Create endpoint"

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-23/a82da585-3241-4033-bc30-996e9f5e7095/ascreenshot.jpeg?tl_px=63,128&br_px=1440,898&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=594,559)
#### [Made with Scribe](https://scribehow.com/shared/Biostatistics_Workshop_-_Step_D_Train_and_Evaluate__g0rnnR8ASCa06azGdAshrQ)


