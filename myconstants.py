import os

# Update USER_DIR, use backslashes '/'
USER_DIR = 'D:/Coding/Python/CmdGPT Prod/User Data'  


PROFILE = 'Profile 7'
DIR = os.getcwd() + '\prompts'
TIMEOUTS = {
    'INIT': 45,
    'RESPONSE': 480
}
SELECTORS = {
    'feedbackBtnsPrefix': "section[class*='ChatMessageActionBar_actionBar_']",
    'clearContextBtn': "button[class*='ChatBreakButton_button_']",
    'inputTextarea': "textarea",
    'allResponseParagraphs': "div[class^='ChatMessagesView_messagePair_']:last-child div[class*='Message_botMessageBubble_'] div[class^='Markdown_markdownContainer_'] > *",
    'firstResponseParagraphs': "div[class^='ChatMessagesView_messagePair_']:last-child>div:last-of-type div[class*='botMessageBubble_'] div[class^='Markdown_markdownContainer_'] > *:first-child",
    'lastCompleteParagraph': "div[class^='ChatMessagesView_messagePair_']:last-child>div:last-of-type div[class*='botMessageBubble_'] div[class^='Markdown_markdownContainer_'] > *:nth-last-child(2)", # second last para
    'lastResponseParagraph': "div[class^='ChatMessagesView_messagePair_']:last-child>div:last-of-type div[class*='botMessageBubble_'] div[class^='Markdown_markdownContainer_'] > *:last-child",
    'responseContainer': "div[class^='ChatMessagesView_messagePair_']:last-child>div:last-of-type div[class^='Markdown_markdownContainer_']"
}
# Total attempts per step
ATTEMPTS = [1, 0, 1]


TEST = [1, 2, 3]