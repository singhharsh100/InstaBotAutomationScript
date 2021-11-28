**Select Raw mode.
# InstaBotAutomationScript
This automated bot works on testing automation tool SELENIUM.
**Make sure the version of chromedriver supports the version of Google chrome that you are using.
Driver--> ChromeDriver 96.0.4664.45
Chrome version--> Version 96.0.4664.45(Latest)

**The bot is not fully working, make sure to read the comments.
Methods:
login-                This method is used to login instagram with your provided credentials
                      **This method makes sure that the browser doesn't remembers the credentials by clicking "Not now" when prompted during login.
mass_like-            This method likes posts which are shown in your instagram feeds.
like_fpost-           This method opens the first post of your feed likes it.
cmnt_post-            This method comments on the respectived post which is opened. 
                      **This method must be used along with *like_fpost method. You can use it elsewhere too according to your needs.
stories-              This method helps you to watch all the insta stories uploaded by people in your following list.
check_msg-            This method replies to the message in your inbox. 
follow-               This methods follows all the people showing in your suggestion until instagram puts a cooldown on the follow button(This method has
                      a sleep timer which waits until the cooldown is over and again starts spamming follow button)
like_all_posts-       This methods likes all the posts of an instagram profile provided to it.
