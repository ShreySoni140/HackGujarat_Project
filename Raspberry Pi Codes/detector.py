from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
import json
import os
files = []

prediction_key = "d0934bbbb5464fafae5976eb82d22365"
ENDPOINT = "https://centralindia.api.cognitive.microsoft.com/"
hey = "12f79bdf-f8ac-4e4a-be4e-14d3feb94169"
publish_iteration_name = "Hack_Final"
# Now there is a trained endpoint that can be used to make a prediction
predictor = CustomVisionPredictionClient(prediction_key, endpoint=ENDPOINT)

# for i in os.listdir("D:\Study Files\Hackathons\MLH Hackathon"):
#     if i.endswith('.jpg'):
base_image_url="D:\img\image.jpg"
with open(base_image_url, "rb") as image_contents:
    results = predictor.classify_image(
        hey, publish_iteration_name, image_contents.read())
    # Display the results.
    for prediction in results.predictions:
        print("\t" + prediction.tag_name +
            ": {0:.2f}%".format(prediction.probability * 100))
        break
		
if prediction.tag_name == "BeltExist" :
	data = []
	t = prediction.tag_name
	data.append({
		'name': t,
		'value': "HIGH"
		})
	with open('data.json', 'w+') as outfile:
		json.dump(data, outfile)
else:
	data = []
	t = prediction.tag_name
	data.append({
		'name': t,
		'value': "LOW"
		})
	with open('data.json', 'w+') as outfile:
		json.dump(data, outfile)

    # end with
files = ['data.json']