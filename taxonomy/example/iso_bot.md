# The ISO37101 bot.

Description: The iso37101 bot is a solution that helps iso auditors prepare audits of cities and mapping of their vision and strategy on the iso37101 reference framework.

The use of the tool aims at making auditors more efficient, especially when processing large texts and large number of texts.

Processes: The tool takes texts as inputs. It processes them using python, and the langchain and openai libraries. The UI is managed using the streamlit tool, and users receive excel sheets and images as outputs. The excel sheet contains the review of the different text, and the audit results under the form of a table. The image(s) are the image of visual representation of the mapping on the ISO37101 reference framework. As such, it uses the ISO standard definitions for all terms used. It optionally can produce Word documents using the template or visual identity of a given client. The processing is using OpenAI model, especially gpt3.5-turbo.

Technically, the tool uses openai "functions calling" to classify text. It also uses LLMs to write up audits results, and explanations of the audit results.

Architecture: The tool uses the streamlit.io platform to deploy webapps. It can also be deployed on any platform using the docker solution to deploy containerized solutions.