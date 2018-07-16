## Generated Story -got everything
* greet
    - utter_greet
    - utter_ask_howcanhelp
* question{"keywords":"removing cognos", "product": "advance process automation", "version": "6.4"}
    - slot{"keywords":"removing cognos"}
    - slot{"product": "advance process automation"}
    - slot{"version": "6.4"}
    - action_search
    - action_suggest
* affirm
    - utter_ask_didthathelp
* affirm
    - utter_thanks
* affirm
    - utter_goodbye
    - action_restart

## Generated Story -got keyword
* greet
    - utter_greet
    - utter_ask_howcanhelp
* question{"keywords":"removing cognos"}
    - slot{"keywords":"removing cognos"}
    - utter_ask_product
* inform{"product": "advance process automation", "version":"6.4"}
    - slot{"product": "advance process automation"}
    - slot{"version": "6.4"}
    - action_search
    - action_suggest
* affirm
    - utter_ask_didthathelp
* affirm
    - utter_thanks
* affirm
    - utter_goodbye
    - action_restart

## Generated Story -got keyword product
* greet
    - utter_greet
    - utter_ask_howcanhelp
* question{"keywords":"removing cognos", "product": "advance process automation"}
    - slot{"keywords":"removing cognos"}
    - slot{"product": "advance process automation"}
    - action_search
    - action_suggest
* affirm
    - utter_ask_didthathelp
* affirm
    - utter_thanks
* affirm
    - utter_goodbye
    - action_restart

## Generated Story -got nothing 1
* greet
    - utter_greet
    - utter_ask_howcanhelp
* question
    - utter_ask_details
* question{"keywords":"removing cognos", "product": "advance process automation"}
    - slot{"keywords":"removing cognos"}
    - slot{"product": "advance process automation"}
    - action_search
    - action_suggest
* affirm
    - utter_ask_didthathelp
* affirm
    - utter_thanks
* affirm
    - utter_goodbye
    - action_restart

## Generated Story -got nothing 2
* greet
    - utter_greet
    - utter_ask_howcanhelp
* question
    - utter_ask_details
* question{"keywords":"removing cognos", "product": "advance process automation"}
    - slot{"keywords":"removing cognos"}
    - slot{"product": "advance process automation"}
    - action_search
    - action_suggest
* affirm
    - utter_ask_didthathelp
* affirm
    - utter_thanks
* affirm
    - utter_goodbye
    - action_restart

## Generated Story -got everything - deny
* greet
    - utter_greet
    - utter_ask_howcanhelp
* question{"keywords":"removing cognos", "product": "advance process automation", "version": "6.4"}
    - slot{"keywords":"removing cognos"}
    - slot{"product": "advance process automation"}
    - slot{"version": "6.4"}
    - action_search
    - action_suggest
* affirm
    - utter_ask_didthathelp
* deny
    - utter_ack_findalternatives
    - utter_ask_version
* inform{"version": "6.4"}
    - slot{"version": "6.4"}
    - utter_ask_details
* inform
    - action_search
    - action_suggest

## Generated Story -got keyword - deny
* greet
    - utter_greet
    - utter_ask_howcanhelp
* question{"keywords":"removing cognos"}
    - slot{"keywords":"removing cognos"}
    - utter_ask_product
* inform{"product": "advance process automation", "version":"6.4"}
    - slot{"product": "advance process automation"}
    - slot{"version": "6.4"}
    - action_search
    - action_suggest
* affirm
    - utter_ask_didthathelp
* deny
    - utter_ack_findalternatives
    - utter_ask_version
* inform{"version": "6.4"}
    - slot{"version": "6.4"}
    - utter_ask_details
* inform
    - action_search
    - action_suggest
* affirm
    - utter_ask_didthathelp
* affirm
    - utter_thanks
* affirm
    - utter_goodbye
    - action_restart

## Generated Story -got keyword product - deny
* greet
    - utter_greet
    - utter_ask_howcanhelp
* question{"keywords":"removing cognos", "product": "advance process automation"}
    - slot{"keywords":"removing cognos"}
    - slot{"product": "advance process automation"}
    - action_search
    - action_suggest
* affirm
    - utter_ask_didthathelp
* deny
    - utter_ack_findalternatives
    - utter_ask_version
* inform{"version": "6.4"}
    - slot{"version": "6.4"}
    - utter_ask_details
* inform
    - action_search
    - action_suggest
* affirm
    - utter_ask_didthathelp
* affirm
    - utter_thanks
* affirm
    - utter_goodbye
    - action_restart

## Generated Story -got nothing - deny
* greet
    - utter_greet
    - utter_ask_howcanhelp
* question
    - utter_ask_details
* question{"keywords":"removing cognos", "product": "advance process automation"}
    - slot{"keywords":"removing cognos"}
    - slot{"product": "advance process automation"}
    - action_search
    - action_suggest
* affirm
    - utter_ask_didthathelp
* deny
    - utter_ack_findalternatives
    - utter_ask_version
* inform{"version": "6.4"}
    - slot{"version": "6.4"}
    - utter_ask_details
* inform
    - action_search
    - action_suggest
* affirm
    - utter_ask_didthathelp
* affirm
    - utter_thanks
* affirm
    - utter_goodbye
    - action_restart

## Generated Story -got nothing 2 - deny
* greet
    - utter_greet
    - utter_ask_howcanhelp
* question
    - utter_ask_details
* question{"keywords":"removing cognos", "product": "advance process automation"}
    - slot{"keywords":"removing cognos"}
    - slot{"product": "advance process automation"}
    - action_search
    - action_suggest
* affirm
    - utter_ask_didthathelp
* deny
    - utter_ack_findalternatives
    - utter_ask_version
* inform{"version": "6.4"}
    - slot{"version": "6.4"}
    - utter_ask_details
* inform
    - action_search
    - action_suggest
* affirm
    - utter_ask_didthathelp
* affirm
    - utter_thanks
* affirm
    - utter_goodbye
    - action_restart

## Generated Story -3839319266746686724
* greet
    - utter_greet
    - utter_ask_howcanhelp
* question{"keywords": "need information about desktop analytics - wfm web services"}
    - slot{"keywords": "need information about desktop analytics - wfm web services"}
    - utter_ask_product
* question{"product": "apa"}
    - slot{"product": "apa"}
    - action_search
    - slot{"matches": [{"id": "17C4F08C-CF7E-E811-801B-543C6C5B470B", "text": "Desktop Analytics - WFM Web Services", "link": "http://www.extranice.com/rts66/#../Subsystems/DesktopAnalytics_Solution/content/rt_rtam_ag/rt_rtam_ag/rtam%20-%20wfm%20web%20services.htm%3FTocPath%3DSolution%2520Deployments%7CDesktop%2520Analytics%2520Solution%7C_____12", "parent": null, "version": "6.6", "rank": 6}, {"id": "B0C8A3C3-CF7E-E811-801B-543C6C5B470B", "text": "Desktop Analytics - WFM Web Services", "link": "http://www.extranice.com/APA67/index.htm#../Subsystems/Desktop_Analytics/content/rt_rtam_ag/rt_rtam_ag/rtam%20-%20wfm%20web%20services.htm%3FTocPath%3DSolution%2520Deployments%7CDesktop%2520Analytics%2520Solution%7C_____12", "parent": null, "version": "6.7", "rank": 6}, {"id": "625CE480-CF7E-E811-801B-543C6C5B470B", "text": "Accessing Desktop Analytics Reports", "link": "http://www.extranice.com/rts66/#../Subsystems/DesktopAnalytics_Solution/content/rtam_user_guide/accessing%20rtam%20reports.htm%3FTocPath%3DSolution%2520Deployments%7CDesktop%2520Analytics%2520Solution%7CDesktop%2520Analytics%2520Reports%7C_____2", "parent": null, "version": "6.6", "rank": 5}]}
    - action_suggest
* thanks
    - utter_ask_didthathelp
* affirm
    - utter_thanks
* question{"keywords": "installing cognos for installations without datamart"}
    - slot{"keywords": "installing cognos for installations without datamart"}
    - action_search
    - slot{"matches": [{"id": "7A8A01DE-CE7E-E811-801B-543C6C5B470B", "text": "Post-Installation Summary Report", "link": "http://www.extranice.com/rts65/#../Subsystems/Server_Install_Upgrade/content/installation/post-installation%20summary%20report.htm%3FTocPath%3DDeployments%7CServer%2520Installation%2520and%2520Upgrade%7CReal-Time%2520Servers%2520-%2520Clean%2520Installation%7C_____9", "parent": "Real-Time Servers - Clean Installation,Server Installation and Upgrade,", "version": "6.5", "rank": 6}, {"id": "1968F9E3-CE7E-E811-801B-543C6C5B470B", "text": "Post-Installation Summary Report", "link": "http://www.extranice.com/rts64/#../Subsystems/Server_Install_Upgrade/content/installation/post-installation%20summary%20report.htm%3FTocPath%3DDeployments%7CServer%2520Installation%2520and%2520Upgrade%7CInstalling%2520Real-Time%2520Servers%2520-%2520Clean%2520Installation%7C_____6", "parent": "Real-Time Servers - Clean Installation,Server Installation and Upgrade,", "version": "6.4", "rank": 6}, {"id": "1CA67803-CF7E-E811-801B-543C6C5B470B", "text": "Post-Installation Summary Report", "link": "http://www.extranice.com/rts65/#../Subsystems/Server_Install_Upgrade/content/installation/post-installation%20summary%20report.htm%3FTocPath%3DDeployments%7CServer%2520Installation%2520and%2520Upgrade%7CReal-Time%2520Servers%2520-%2520Clean%2520Installation%7C_____9", "parent": "Real-Time Servers - Clean Installation,Server Installation and Upgrade,", "version": "6.5", "rank": 6}]}
    - action_suggest
* thanks
    - utter_ask_didthathelp
* affirm
    - utter_thanks
* goodbye
    - utter_goodbye
    - export

## Generated Story 6347966984759475914
* question
    - utter_ask_howcanhelp
* question{"keywords": "asked who"}
    - slot{"keywords": "asked who"}
    - utter_ask_details
* question{"keywords": "configure application policies ?"}
    - slot{"keywords": "configure application policies ?"}
    - action_search
    - slot{"matches": [{"id": "DE5BE480-CF7E-E811-801B-543C6C5B470B", "text": "Configuring the Application Policies", "link": "http://www.extranice.com/rts66/#../Subsystems/RA_Solution_Guide/content/topics%20-%20robotic%20automation/configuring%20application%20authorization.htm%3FTocPath%3DSolution%2520Deployments%7CRobotic%2520Automation%2520Solution%2520%7CConfiguring%2520OpenAM%2520%7C_____5", "parent": null, "version": "6.6", "rank": 8}, {"id": "4A8B01DE-CE7E-E811-801B-543C6C5B470B", "text": "Configuring the Application", "link": "http://www.extranice.com/rts65/#../Subsystems/System_Administration/content/rt_system_admin/configuring%20the%20application.htm#real_time_server_administration_2713896074_1194602%3FTocPath%3DConfigurations%7CSystem%2520Administration%7CReal-Time%2520Server%2520Administration%7CApplication%2520Server%2520Deployment%2520and%2520Configuration%7C_____3", "parent": "Application Server Deployment and Configuration,Real-Time Server Administration,System Administration,", "version": "6.5", "rank": 7}, {"id": "2269F9E3-CE7E-E811-801B-543C6C5B470B", "text": "Configuring the Application", "link": "http://www.extranice.com/rts64/#../Subsystems/System_Administration/content/rt_system_admin/configuring%20the%20application.htm#real_time_server_administration_2713896074_1194602%3FTocPath%3DConfigurations%7CSystem%2520Administration%7CReal-Time%2520Server%2520Administration%7CApplication%2520Server%2520Deployment%2520and%2520Configuration%7C_____3", "parent": "Application Server Deployment and Configuration,Real-Time Server Administration,System Administration,", "version": "6.4", "rank": 7}]}
    - action_suggest
    - utter_ask_didthathelp
    - utter_ask_didthathelp
* affirm
    - utter_thanks
* question
    - utter_ask_didthathelp
* deny
    - utter_ack_findalternatives
    - utter_ask_version
* inform
    - utter_ask_details
* question{"keywords": "configuring the application policies"}
    - slot{"keywords": "configuring the application policies"}
    - action_search
    - slot{"matches": [{"id": "EC68F9E3-CE7E-E811-801B-543C6C5B470B", "text": "Application Logs", "link": "http://www.extranice.com/rts64/#../Subsystems/RTS_Maintenance/content/rt_system_admin/application%20logs.htm#real_time_server_administration_2713896074_1258130%3FTocPath%3DConfigurations%7CReal-Time%2520Maintenance%7CReal-Time%2520Server%7CViewing%2520Server%2520Logs%7C_____2", "parent": "Server Logs,Real-Time Server Administration,System Administration,", "version": "6.4", "rank": 7}, {"id": "4E69F9E3-CE7E-E811-801B-543C6C5B470B", "text": "Application Logs", "link": "http://www.extranice.com/rts64/#../Subsystems/System_Administration/content/rt_system_admin/application%20logs.htm#real_time_server_administration_2713896074_1258130%3FTocPath%3DConfigurations%7CSystem%2520Administration%7CReal-Time%2520Server%2520Administration%7CServer%2520Logs%7C_____2", "parent": "Server Logs,Real-Time Server Administration,System Administration,", "version": "6.4", "rank": 7}, {"id": "788B01DE-CE7E-E811-801B-543C6C5B470B", "text": "Application Server Logs", "link": "http://www.extranice.com/rts65/#../Subsystems/System_Administration/content/rt_system_admin/application%20server%20logs1.htm#real_time_server_administration_2713896074_1258439%3FTocPath%3DConfigurations%7CSystem%2520Administration%7CReal-Time%2520Server%2520Administration%7CServer%2520Logs%7C_____3", "parent": "Server Logs,Real-Time Server Administration,System Administration,", "version": "6.5", "rank": 6}]}
    - action_suggest
* thanks
    - utter_ask_didthathelp
* thanks
    - utter_thanks
* goodbye
    - utter_goodbye
    - export

