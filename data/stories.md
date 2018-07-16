## Generated Story -got everything
* greet
    - utter_greet
* question{"keywords":"removing cognos", "product": "advance process automation", "version": "6.4"}
    - slot{"keywords":"removing cognos"}
    - slot{"product": "advance process automation"}
    - slot{"version": "6.4"}
    - action_search
    - action_suggest
    - utter_ask_didthathelp
* affirm
    - utter_thanks
* affirm
    - utter_goodbye
    - action_restart

## Generated Story -got keyword
* greet
    - utter_greet

* question{"keywords":"removing cognos"}
    - slot{"keywords":"removing cognos"}
    - utter_ask_product
* inform{"product": "advance process automation", "version":"6.4"}
    - slot{"product": "advance process automation"}
    - slot{"version": "6.4"}
    - action_search
    - action_suggest
    - utter_ask_didthathelp
* affirm
    - utter_thanks
* affirm
    - utter_goodbye
    - action_restart

## Generated Story -got keyword product
* greet
    - utter_greet

* question{"keywords":"removing cognos", "product": "advance process automation"}
    - slot{"keywords":"removing cognos"}
    - slot{"product": "advance process automation"}
    - action_search
    - action_suggest     
    - utter_ask_didthathelp
* affirm
    - utter_thanks
* affirm
    - utter_goodbye
    - action_restart

## Generated Story -got nothing 1
* greet
    - utter_greet

* question
    - utter_ask_details
* question{"keywords":"removing cognos", "product": "advance process automation"}
    - slot{"keywords":"removing cognos"}
    - slot{"product": "advance process automation"}
    - action_search
    - action_suggest     
    - utter_ask_didthathelp
* affirm
    - utter_thanks
* affirm
    - utter_goodbye
    - action_restart

## Generated Story -got nothing 2
* greet
    - utter_greet

* question
    - utter_ask_details
* question{"keywords":"removing cognos", "product": "advance process automation"}
    - slot{"keywords":"removing cognos"}
    - slot{"product": "advance process automation"}
    - action_search
    - action_suggest     
    - utter_ask_didthathelp
* affirm
    - utter_thanks
* affirm
    - utter_goodbye
    - action_restart

## Generated Story -got everything - deny
* greet
    - utter_greet

* question{"keywords":"removing cognos", "product": "advance process automation", "version": "6.4"}
    - slot{"keywords":"removing cognos"}
    - slot{"product": "advance process automation"}
    - slot{"version": "6.4"}
    - action_search
    - action_suggest     
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
    - utter_ask_didthathelp
* affirm
    - utter_thanks
* goodbye
    - utter_goodbye
    - action_restart

## Generated Story -got keyword - deny
* greet
    - utter_greet

* question{"keywords":"removing cognos"}
    - slot{"keywords":"removing cognos"}
    - utter_ask_product
* inform{"product": "advance process automation", "version":"6.4"}
    - slot{"product": "advance process automation"}
    - slot{"version": "6.4"}
    - action_search
    - action_suggest     
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
    - utter_ask_didthathelp
* affirm
    - utter_thanks
* affirm
    - utter_goodbye
    - action_restart

## Generated Story -got keyword product - deny
* greet
    - utter_greet

* question{"keywords":"removing cognos", "product": "advance process automation"}
    - slot{"keywords":"removing cognos"}
    - slot{"product": "advance process automation"}
    - action_search
    - action_suggest     
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
    - utter_ask_didthathelp
* affirm
    - utter_thanks
* affirm
    - utter_goodbye
    - action_restart

## Generated Story -got nothing - deny
* greet
    - utter_greet

* question
    - utter_ask_details
* question{"keywords":"removing cognos", "product": "advance process automation"}
    - slot{"keywords":"removing cognos"}
    - slot{"product": "advance process automation"}
    - action_search
    - action_suggest     
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
    - utter_ask_didthathelp
* affirm
    - utter_thanks
* affirm
    - utter_goodbye
    - action_restart

## Generated Story -got nothing 2 - deny
* greet
    - utter_greet

* question
    - utter_ask_details
* question{"keywords":"removing cognos", "product": "advance process automation"}
    - slot{"keywords":"removing cognos"}
    - slot{"product": "advance process automation"}
    - action_search
    - action_suggest     
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
    - utter_ask_didthathelp
* affirm
    - utter_thanks
* affirm
    - utter_goodbye
    - action_restart

## Generated Story -3839319266746686724
* greet
    - utter_greet

* question{"keywords": "need information about desktop analytics - wfm web services"}
    - slot{"keywords": "need information about desktop analytics - wfm web services"}
    - utter_ask_product
* question{"product": "apa"}
    - slot{"product": "apa"}
    - action_search
    - slot{"matches": [{"id": "17C4F08C-CF7E-E811-801B-543C6C5B470B", "text": "Desktop Analytics - WFM Web Services", "link": "http://www.extranice.com/rts66/#../Subsystems/DesktopAnalytics_Solution/content/rt_rtam_ag/rt_rtam_ag/rtam%20-%20wfm%20web%20services.htm%3FTocPath%3DSolution%2520Deployments%7CDesktop%2520Analytics%2520Solution%7C_____12", "parent": null, "version": "6.6", "rank": 6}, {"id": "B0C8A3C3-CF7E-E811-801B-543C6C5B470B", "text": "Desktop Analytics - WFM Web Services", "link": "http://www.extranice.com/APA67/index.htm#../Subsystems/Desktop_Analytics/content/rt_rtam_ag/rt_rtam_ag/rtam%20-%20wfm%20web%20services.htm%3FTocPath%3DSolution%2520Deployments%7CDesktop%2520Analytics%2520Solution%7C_____12", "parent": null, "version": "6.7", "rank": 6}, {"id": "625CE480-CF7E-E811-801B-543C6C5B470B", "text": "Accessing Desktop Analytics Reports", "link": "http://www.extranice.com/rts66/#../Subsystems/DesktopAnalytics_Solution/content/rtam_user_guide/accessing%20rtam%20reports.htm%3FTocPath%3DSolution%2520Deployments%7CDesktop%2520Analytics%2520Solution%7CDesktop%2520Analytics%2520Reports%7C_____2", "parent": null, "version": "6.6", "rank": 5}]}
    - action_suggest     
    - utter_ask_didthathelp
* thanks
    - utter_thanks
    - utter_anything_else
* question{"keywords": "installing cognos for installations without datamart"}
    - slot{"keywords": "installing cognos for installations without datamart"}
    - action_search
    - slot{"matches": [{"id": "7A8A01DE-CE7E-E811-801B-543C6C5B470B", "text": "Post-Installation Summary Report", "link": "http://www.extranice.com/rts65/#../Subsystems/Server_Install_Upgrade/content/installation/post-installation%20summary%20report.htm%3FTocPath%3DDeployments%7CServer%2520Installation%2520and%2520Upgrade%7CReal-Time%2520Servers%2520-%2520Clean%2520Installation%7C_____9", "parent": "Real-Time Servers - Clean Installation,Server Installation and Upgrade,", "version": "6.5", "rank": 6}, {"id": "1968F9E3-CE7E-E811-801B-543C6C5B470B", "text": "Post-Installation Summary Report", "link": "http://www.extranice.com/rts64/#../Subsystems/Server_Install_Upgrade/content/installation/post-installation%20summary%20report.htm%3FTocPath%3DDeployments%7CServer%2520Installation%2520and%2520Upgrade%7CInstalling%2520Real-Time%2520Servers%2520-%2520Clean%2520Installation%7C_____6", "parent": "Real-Time Servers - Clean Installation,Server Installation and Upgrade,", "version": "6.4", "rank": 6}, {"id": "1CA67803-CF7E-E811-801B-543C6C5B470B", "text": "Post-Installation Summary Report", "link": "http://www.extranice.com/rts65/#../Subsystems/Server_Install_Upgrade/content/installation/post-installation%20summary%20report.htm%3FTocPath%3DDeployments%7CServer%2520Installation%2520and%2520Upgrade%7CReal-Time%2520Servers%2520-%2520Clean%2520Installation%7C_____9", "parent": "Real-Time Servers - Clean Installation,Server Installation and Upgrade,", "version": "6.5", "rank": 6}]}
    - action_suggest     
    - utter_ask_didthathelp
* thanks
    - utter_thanks
    - utter_anything_else
* deny
    - utter_goodbye
    - action_restart

## Generated Story 6347966984759475914
* question
    - utter_ask_howcanhelp
* question
    - utter_ask_details
* question{"keywords": "configure application policies ?"}
    - slot{"keywords": "configure application policies ?"}
    - action_search
    - slot{"matches": [{"id": "DE5BE480-CF7E-E811-801B-543C6C5B470B", "text": "Configuring the Application Policies", "link": "http://www.extranice.com/rts66/#../Subsystems/RA_Solution_Guide/content/topics%20-%20robotic%20automation/configuring%20application%20authorization.htm%3FTocPath%3DSolution%2520Deployments%7CRobotic%2520Automation%2520Solution%2520%7CConfiguring%2520OpenAM%2520%7C_____5", "parent": null, "version": "6.6", "rank": 8}, {"id": "4A8B01DE-CE7E-E811-801B-543C6C5B470B", "text": "Configuring the Application", "link": "http://www.extranice.com/rts65/#../Subsystems/System_Administration/content/rt_system_admin/configuring%20the%20application.htm#real_time_server_administration_2713896074_1194602%3FTocPath%3DConfigurations%7CSystem%2520Administration%7CReal-Time%2520Server%2520Administration%7CApplication%2520Server%2520Deployment%2520and%2520Configuration%7C_____3", "parent": "Application Server Deployment and Configuration,Real-Time Server Administration,System Administration,", "version": "6.5", "rank": 7}, {"id": "2269F9E3-CE7E-E811-801B-543C6C5B470B", "text": "Configuring the Application", "link": "http://www.extranice.com/rts64/#../Subsystems/System_Administration/content/rt_system_admin/configuring%20the%20application.htm#real_time_server_administration_2713896074_1194602%3FTocPath%3DConfigurations%7CSystem%2520Administration%7CReal-Time%2520Server%2520Administration%7CApplication%2520Server%2520Deployment%2520and%2520Configuration%7C_____3", "parent": "Application Server Deployment and Configuration,Real-Time Server Administration,System Administration,", "version": "6.4", "rank": 7}]}
    - action_suggest
    - utter_ask_didthathelp
* affirm
    - utter_thanks
* question
    - utter_ask_didthathelp
* deny
    - utter_ack_findalternatives
    - utter_ask_version
* deny
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
    - action_restart

## Generated Story 63479669847594759129
* question
    - utter_ask_howcanhelp
* question
    - utter_ask_details
* question{"keywords": "configure application policies ?"}
    - slot{"keywords": "configure application policies ?"}
    - action_search
    - slot{"matches": [{"id": "DE5BE480-CF7E-E811-801B-543C6C5B470B", "text": "Configuring the Application Policies", "link": "http://www.extranice.com/rts66/#../Subsystems/RA_Solution_Guide/content/topics%20-%20robotic%20automation/configuring%20application%20authorization.htm%3FTocPath%3DSolution%2520Deployments%7CRobotic%2520Automation%2520Solution%2520%7CConfiguring%2520OpenAM%2520%7C_____5", "parent": null, "version": "6.6", "rank": 8}, {"id": "4A8B01DE-CE7E-E811-801B-543C6C5B470B", "text": "Configuring the Application", "link": "http://www.extranice.com/rts65/#../Subsystems/System_Administration/content/rt_system_admin/configuring%20the%20application.htm#real_time_server_administration_2713896074_1194602%3FTocPath%3DConfigurations%7CSystem%2520Administration%7CReal-Time%2520Server%2520Administration%7CApplication%2520Server%2520Deployment%2520and%2520Configuration%7C_____3", "parent": "Application Server Deployment and Configuration,Real-Time Server Administration,System Administration,", "version": "6.5", "rank": 7}, {"id": "2269F9E3-CE7E-E811-801B-543C6C5B470B", "text": "Configuring the Application", "link": "http://www.extranice.com/rts64/#../Subsystems/System_Administration/content/rt_system_admin/configuring%20the%20application.htm#real_time_server_administration_2713896074_1194602%3FTocPath%3DConfigurations%7CSystem%2520Administration%7CReal-Time%2520Server%2520Administration%7CApplication%2520Server%2520Deployment%2520and%2520Configuration%7C_____3", "parent": "Application Server Deployment and Configuration,Real-Time Server Administration,System Administration,", "version": "6.4", "rank": 7}]}
    - action_suggest
    - utter_ask_didthathelp
* affirm
    - utter_thanks
* question
    - utter_ask_didthathelp
* deny
    - utter_ack_findalternatives
    - utter_ask_version
* affirm
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
    - action_restart



## Generated Story 3468442584282918712
* question{"product": "apa"}
    - slot{"product": "apa"}
    - action_search
    - action_suggest
    - utter_anything_else
* question{"keywords": "need help with installing ssis on the cluster environment"}
    - slot{"keywords": "need help with installing ssis on the cluster environment"}
    - action_search
    - slot{"matches": [{"id": "D692EB7A-CF7E-E811-801B-543C6C5B470B", "text": "Installing SSIS on the Cluster Environment", "link": "http://www.extranice.com/rts66/#../Subsystems/RTS%20High%20Availability/content/topics/installing%20ssis%20on%20the%20cluster%20environment.htm%3FTocPath%3DDeployments%7CHigh%2520Availability%7C_____9", "parent": null, "version": "6.6", "rank": 7}, {"id": "9FC8A3C3-CF7E-E811-801B-543C6C5B470B", "text": "Installing SSIS on the Cluster Environment", "link": "http://www.extranice.com/APA67/index.htm#../Subsystems/High_Availability/content/topics/installing%20ssis%20on%20the%20cluster%20environment.htm%3FTocPath%3DDeployments%7CHigh%2520Availability%7CSQL%2520Failover%2520-%2520Cluster%2520Disk%2520Replication%7C_____2", "parent": null, "version": "6.7", "rank": 7}, {"id": "708A01DE-CE7E-E811-801B-543C6C5B470B", "text": "Uninstalling the SNMP Agent", "link": "http://www.extranice.com/rts65/#../Subsystems/Server_Install_Upgrade/content/installation/uninstalling%20the%20snmp%20agent.htm%3FTocPath%3DDeployments%7CServer%2520Installation%2520and%2520Upgrade%7CReal-Time%2520Servers%2520-%2520Clean%2520Installation%7C(Optional)%2520Sentinel%2520SNMP%2520Agent%2520Installation%7C_____3", "parent": "(Optional) Sentinel SNMP Agent Installation,Real-Time Servers - Clean Installation,Server Installation and Upgrade,", "version": "6.5", "rank": 5}]}
    - action_suggest
    - utter_ask_didthathelp
* affirm
    - utter_thanks
    - utter_anything_else
* question{"keywords": "configuring adapters and bindings"}
    - slot{"keywords": "configuring adapters and bindings"}
    - action_search
    - slot{"matches": [{"id": "CC92EB7A-CF7E-E811-801B-543C6C5B470B", "text": "Configuring Adapters and Bindings", "link": "http://www.extranice.com/rts66/#../Subsystems/RTS%20High%20Availability/content/cluster_install_config-engage/configuring%20adapters%20and%20bindings%20.htm%3FTocPath%3DDeployments%7CHigh%2520Availability%7CMicrosoft%2520Cluster%2520Installation%7CMicrosoft%2520Cluster%2520Installation%2520and%2520Configuration%7CConfiguring%2520the%2520Public%2520and%2520Private%2520Networks%7CConfiguring%2520the%2520Private%2520and%2520Public%2520Network%2520Adapters%7C_____3", "parent": null, "version": "6.6", "rank": 9}, {"id": "1C8D01DE-CE7E-E811-801B-543C6C5B470B", "text": "Configuring Tasks", "link": "http://www.extranice.com/rts65/#../Subsystems/RTAM_Solution/content/rtam_user_guide/configuring%20tasks.htm%3FTocPath%3DSolution%2520Deployments%7CRTAM%2520(Real-Time%2520Activity%2520Monitoring)%2520Solution%7CApplication%2520and%2520Process%2520Monitoring%2520in%2520Real-Time%2520Designer%7CDefining%2520Process%2520Monitoring%2520in%2520Real-Time%2520Designer%7CConfiguring%2520a%2520Process%2520and%2520Its%2520Tasks%7C_____3", "parent": "Configuring a Process and Its Tasks,Defining Process Monitoring in Real-Time Designer,Application Monitoring in Real-Time Designer,RTAM (Real-Time Activity Monitoring) Solution,", "version": "6.5", "rank": 6}, {"id": "3667F9E3-CE7E-E811-801B-543C6C5B470B", "text": "Configuring the Logging Settings", "link": "http://www.extranice.com/rts65/#../Subsystems/Designer_User/content/designer_ug/configuring%20the%20logging%20settings.htm%3FTocPath%3DUsers%7CDesigner%2520User%7CTroubleshooting%2520Using%2520Logs%7C_____2", "parent": "Troubleshooting Using Logs,Designer User,", "version": "6.5", "rank": 6}]}
    - action_suggest
    - utter_ask_didthathelp
* affirm
    - utter_thanks
    - utter_anything_else
* deny
    - utter_goodbye
    - action_restart

## Generated Story 3468442584282918712r2
* question{"product": "apa"}
    - slot{"product": "apa"}
    - utter_product_page
    - utter_anything_else
* question{"keywords": "need help with installing ssis on the cluster environment"}
    - slot{"keywords": "need help with installing ssis on the cluster environment"}
    - action_search
    - slot{"matches": [{"id": "D692EB7A-CF7E-E811-801B-543C6C5B470B", "text": "Installing SSIS on the Cluster Environment", "link": "http://www.extranice.com/rts66/#../Subsystems/RTS%20High%20Availability/content/topics/installing%20ssis%20on%20the%20cluster%20environment.htm%3FTocPath%3DDeployments%7CHigh%2520Availability%7C_____9", "parent": null, "version": "6.6", "rank": 7}, {"id": "9FC8A3C3-CF7E-E811-801B-543C6C5B470B", "text": "Installing SSIS on the Cluster Environment", "link": "http://www.extranice.com/APA67/index.htm#../Subsystems/High_Availability/content/topics/installing%20ssis%20on%20the%20cluster%20environment.htm%3FTocPath%3DDeployments%7CHigh%2520Availability%7CSQL%2520Failover%2520-%2520Cluster%2520Disk%2520Replication%7C_____2", "parent": null, "version": "6.7", "rank": 7}, {"id": "708A01DE-CE7E-E811-801B-543C6C5B470B", "text": "Uninstalling the SNMP Agent", "link": "http://www.extranice.com/rts65/#../Subsystems/Server_Install_Upgrade/content/installation/uninstalling%20the%20snmp%20agent.htm%3FTocPath%3DDeployments%7CServer%2520Installation%2520and%2520Upgrade%7CReal-Time%2520Servers%2520-%2520Clean%2520Installation%7C(Optional)%2520Sentinel%2520SNMP%2520Agent%2520Installation%7C_____3", "parent": "(Optional) Sentinel SNMP Agent Installation,Real-Time Servers - Clean Installation,Server Installation and Upgrade,", "version": "6.5", "rank": 5}]}
    - action_suggest
    - utter_ask_didthathelp
* affirm
    - utter_thanks
    - utter_anything_else
* question{"keywords": "configuring adapters and bindings"}
    - slot{"keywords": "configuring adapters and bindings"}
    - action_search
    - slot{"matches": [{"id": "CC92EB7A-CF7E-E811-801B-543C6C5B470B", "text": "Configuring Adapters and Bindings", "link": "http://www.extranice.com/rts66/#../Subsystems/RTS%20High%20Availability/content/cluster_install_config-engage/configuring%20adapters%20and%20bindings%20.htm%3FTocPath%3DDeployments%7CHigh%2520Availability%7CMicrosoft%2520Cluster%2520Installation%7CMicrosoft%2520Cluster%2520Installation%2520and%2520Configuration%7CConfiguring%2520the%2520Public%2520and%2520Private%2520Networks%7CConfiguring%2520the%2520Private%2520and%2520Public%2520Network%2520Adapters%7C_____3", "parent": null, "version": "6.6", "rank": 9}, {"id": "1C8D01DE-CE7E-E811-801B-543C6C5B470B", "text": "Configuring Tasks", "link": "http://www.extranice.com/rts65/#../Subsystems/RTAM_Solution/content/rtam_user_guide/configuring%20tasks.htm%3FTocPath%3DSolution%2520Deployments%7CRTAM%2520(Real-Time%2520Activity%2520Monitoring)%2520Solution%7CApplication%2520and%2520Process%2520Monitoring%2520in%2520Real-Time%2520Designer%7CDefining%2520Process%2520Monitoring%2520in%2520Real-Time%2520Designer%7CConfiguring%2520a%2520Process%2520and%2520Its%2520Tasks%7C_____3", "parent": "Configuring a Process and Its Tasks,Defining Process Monitoring in Real-Time Designer,Application Monitoring in Real-Time Designer,RTAM (Real-Time Activity Monitoring) Solution,", "version": "6.5", "rank": 6}, {"id": "3667F9E3-CE7E-E811-801B-543C6C5B470B", "text": "Configuring the Logging Settings", "link": "http://www.extranice.com/rts65/#../Subsystems/Designer_User/content/designer_ug/configuring%20the%20logging%20settings.htm%3FTocPath%3DUsers%7CDesigner%2520User%7CTroubleshooting%2520Using%2520Logs%7C_____2", "parent": "Troubleshooting Using Logs,Designer User,", "version": "6.5", "rank": 6}]}
    - action_suggest
    - utter_ask_didthathelp
* affirm
    - utter_thanks
    - utter_anything_else
* deny
    - utter_goodbye
    - action_restart



## Generated Story -4251130625937000762
* greet
    - utter_greet
* question{"keywords": "extra terminal service functionality ?"}
    - slot{"keywords": "extra terminal service functionality ?"}
    - utter_ask_product
* inform{"product": "rts"}
    - slot{"product": "rts"}
    - action_search
    - slot{"matches": [{"id": "7C6BF9E3-CE7E-E811-801B-543C6C5B470B", "text": "Extra Terminal Service Functionality", "link": "http://www.extranice.com/rts64/#../Subsystems/Designer_User/content/designer_ug/extra%20terminal%20service%20functionality.htm%3FTocPath%3DUsers%7CDesigner%2520User%7CPhysical%2520Objects%7CUsing%2520an%2520Extra%2520Terminal%2520Service%7C_____3", "parent": "Using an Extra Terminal Service,Physical Objects,Designer User,", "version": "6.4", "rank": 9}, {"id": "088E01DE-CE7E-E811-801B-543C6C5B470B", "text": "Extra Terminal and Extra Terminal Permanent Connection Service Functionality", "link": "http://www.extranice.com/rts65/#../Subsystems/Designer_User/content/designer_ug/extra%20terminal%20service%20functionality.htm%3FTocPath%3DUsers%7CDesigner%2520User%7CPhysical%2520Objects%7CUsing%2520an%2520Extra%2520Terminal%2520or%2520ExtraTerminal%2520Permanent%2520Connection%2520Service%7C_____3", "parent": "Using an Extra Terminal or ExtraTerminal Permanent Connection Service,Physical Objects,Designer User,", "version": "6.5", "rank": 6}, {"id": "7B6BF9E3-CE7E-E811-801B-543C6C5B470B", "text": "Defining an Extra Terminal Service", "link": "http://www.extranice.com/rts64/#../Subsystems/Designer_User/content/designer_ug/defining%20an%20extra%20terminal%20service.htm%3FTocPath%3DUsers%7CDesigner%2520User%7CPhysical%2520Objects%7CUsing%2520an%2520Extra%2520Terminal%2520Service%7C_____2", "parent": "Using an Extra Terminal Service,Physical Objects,Designer User,", "version": "6.4", "rank": 6}]}
    - action_suggest
    - utter_ask_didthathelp
* affirm
    - utter_thanks
    - utter_anything_else
* affirm
* question{"keywords": "run scripts on your databases?"}
    - slot{"keywords": "run scripts on your databases?"}
    - action_search
    - slot{"matches": [{"id": "A68A01DE-CE7E-E811-801B-543C6C5B470B", "text": "Run Scripts on Your Databases", "link": "http://www.extranice.com/rts65/#../Subsystems/Server_Install_Upgrade/content/run%20scripts%20on%20your%20databases.htm%3FTocPath%3DDeployments%7CServer%2520Installation%2520and%2520Upgrade%7CUpgrading%2520from%2520R4.9%2520and%2520Above%2520to%2520R6.5%7C_____8", "parent": "Upgrading from R4.9 and Above to R6.5,Server Installation and Upgrade,", "version": "6.5", "rank": 8}, {"id": "48A67803-CF7E-E811-801B-543C6C5B470B", "text": "Run Scripts on Your Databases", "link": "http://www.extranice.com/rts65/#../Subsystems/Server_Install_Upgrade/content/run%20scripts%20on%20your%20databases.htm%3FTocPath%3DDeployments%7CServer%2520Installation%2520and%2520Upgrade%7CUpgrading%2520from%2520R4.9%2520and%2520Above%2520to%2520R6.5%7C_____8", "parent": "Upgrading from R4.9 and Above to R6.5,Server Installation and Upgrade,", "version": "6.5", "rank": 8}, {"id": "FC59E480-CF7E-E811-801B-543C6C5B470B", "text": "Run Scripts on Your Databases", "link": "http://www.extranice.com/rts66/#../Subsystems/Server_Install_Upgrade/content/topics/run%20scripts%20on%20your%20databases.htm%3FTocPath%3DDeployments%7CServer%2520Installation%2520and%2520Upgrade%7CUpgrading%2520from%2520R4.9%2520and%2520Above%2520to%2520R6.5%2520and%2520Above%7C_____8", "parent": "Upgrading from R4.9 and Above to R6.5,Server Installation and Upgrade,", "version": "6.6", "rank": 8}]}
    - action_suggest
    - utter_ask_didthathelp
* affirm
    - utter_thanks
    - utter_anything_else
* deny
    - utter_goodbye
    - action_restart

## Generated Story 4523785906473642747
* question
    - utter_greet
* question
    - utter_ask_details
* question
    - utter_structured_garbage
    - utter_ask_details
* question{"keywords": "use the reports to analyze the cause for spikes in productivity"}
    - slot{"keywords": "use the reports to analyze the cause for spikes in productivity"}
    - action_search
    - slot{"matches": [{"id": "8E8D01DE-CE7E-E811-801B-543C6C5B470B", "text": "Use the Reports to Analyze the Cause for Spikes in Productivity", "link": "http://www.extranice.com/rts65/#../Subsystems/RTAM_Solution/content/rtam_user_guide/use%20the%20reports%20to%20analyze%20the%20cause%20for%20spikes%20in%20productivity.htm#rtam_best_practices_3277801691_1569312%3FTocPath%3DSolution%2520Deployments%7CRTAM%2520(Real-Time%2520Activity%2520Monitoring)%2520Solution%7CRTAM%2520Best%2520Practices%7CPerform%2520Routine%2520RTAM%2520Activities%7C_____1", "parent": "Perform Routine RTAM Activities,RTAM Best Practices,RTAM (Real-Time Activity Monitoring) Solution,", "version": "6.5", "rank": 9}, {"id": "30A97803-CF7E-E811-801B-543C6C5B470B", "text": "Use the Reports to Analyze the Cause for Spikes in Productivity", "link": "http://www.extranice.com/rts65/#../Subsystems/RTAM_Solution/content/rtam_user_guide/use%20the%20reports%20to%20analyze%20the%20cause%20for%20spikes%20in%20productivity.htm#rtam_best_practices_3277801691_1569312%3FTocPath%3DSolution%2520Deployments%7CRTAM%2520(Real-Time%2520Activity%2520Monitoring)%2520Solution%7CRTAM%2520Best%2520Practices%7CPerform%2520Routine%2520RTAM%2520Activities%7C_____1", "parent": "Perform Routine RTAM Activities,RTAM Best Practices,RTAM (Real-Time Activity Monitoring) Solution,", "version": "6.5", "rank": 9}, {"id": "10C4F08C-CF7E-E811-801B-543C6C5B470B", "text": "Use the Reports to Analyze the Cause for Spikes in Productivity", "link": "http://www.extranice.com/rts66/#../Subsystems/DesktopAnalytics_Solution/content/rtam_user_guide/use%20the%20reports%20to%20analyze%20the%20cause%20for%20spikes%20in%20productivity.htm#rtam_best_practices_3277801691_1569312%3FTocPath%3DSolution%2520Deployments%7CDesktop%2520Analytics%2520Solution%7CDesktop%2520Analytics%2520Best%2520Practices%7CPerform%2520Routine%2520Desktop%2520Analytics%2520Activities%7C_____1", "parent": "Perform Routine RTAM Activities,RTAM Best Practices,RTAM (Real-Time Activity Monitoring) Solution,", "version": "6.6", "rank": 9}]}
    - action_suggest
    - utter_ask_didthathelp
* deny
    - utter_ask_product
* inform{"product": "rts"}
    - slot{"product": "rts"}
    - utter_ask_version
* inform{"version": "6.5"}
    - slot{"version": "6.5"}
    - action_search
    - slot{"matches": [{"id": "8E8D01DE-CE7E-E811-801B-543C6C5B470B", "text": "Use the Reports to Analyze the Cause for Spikes in Productivity", "link": "http://www.extranice.com/rts65/#../Subsystems/RTAM_Solution/content/rtam_user_guide/use%20the%20reports%20to%20analyze%20the%20cause%20for%20spikes%20in%20productivity.htm#rtam_best_practices_3277801691_1569312%3FTocPath%3DSolution%2520Deployments%7CRTAM%2520(Real-Time%2520Activity%2520Monitoring)%2520Solution%7CRTAM%2520Best%2520Practices%7CPerform%2520Routine%2520RTAM%2520Activities%7C_____1", "parent": "Perform Routine RTAM Activities,RTAM Best Practices,RTAM (Real-Time Activity Monitoring) Solution,", "version": "6.5", "rank": 9}, {"id": "30A97803-CF7E-E811-801B-543C6C5B470B", "text": "Use the Reports to Analyze the Cause for Spikes in Productivity", "link": "http://www.extranice.com/rts65/#../Subsystems/RTAM_Solution/content/rtam_user_guide/use%20the%20reports%20to%20analyze%20the%20cause%20for%20spikes%20in%20productivity.htm#rtam_best_practices_3277801691_1569312%3FTocPath%3DSolution%2520Deployments%7CRTAM%2520(Real-Time%2520Activity%2520Monitoring)%2520Solution%7CRTAM%2520Best%2520Practices%7CPerform%2520Routine%2520RTAM%2520Activities%7C_____1", "parent": "Perform Routine RTAM Activities,RTAM Best Practices,RTAM (Real-Time Activity Monitoring) Solution,", "version": "6.5", "rank": 9}, {"id": "10C4F08C-CF7E-E811-801B-543C6C5B470B", "text": "Use the Reports to Analyze the Cause for Spikes in Productivity", "link": "http://www.extranice.com/rts66/#../Subsystems/DesktopAnalytics_Solution/content/rtam_user_guide/use%20the%20reports%20to%20analyze%20the%20cause%20for%20spikes%20in%20productivity.htm#rtam_best_practices_3277801691_1569312%3FTocPath%3DSolution%2520Deployments%7CDesktop%2520Analytics%2520Solution%7CDesktop%2520Analytics%2520Best%2520Practices%7CPerform%2520Routine%2520Desktop%2520Analytics%2520Activities%7C_____1", "parent": "Perform Routine RTAM Activities,RTAM Best Practices,RTAM (Real-Time Activity Monitoring) Solution,", "version": "6.6", "rank": 9}]}
    - action_suggest
    - utter_ask_didthathelp
* affirm
    - utter_thanks
    - utter_anything_else
* deny
    - utter_thanks
    - utter_goodbye
    - action_restart

## Generated Story 1895130752058533944
* deny
    - utter_greet
* question
    - utter_ask_details
* question
    - utter_ask_details
* deny
    - utter_structured_garbage
    - utter_ask_details
* deny
    - utter_structured_garbage
    - utter_ask_details
* affirm
    - utter_structured_garbage
    - utter_ask_details
* question{"keywords": "aboyut", "product": "apa", "version": "6.7"}
    - slot{"keywords": "aboyut"}
    - slot{"product": "apa"}
    - slot{"version": "6.7"}
    - action_search
    - slot{"matches": [{"id": "1F8B01DE-CE7E-E811-801B-543C6C5B470B", "text": "Callouts", "link": "http://www.extranice.com/rts65/#../Subsystems/Data%20Collection%20Cognos/content/collecting%20and%20viewing%20data%20in%20cognos%20quick%20guide%20draft8/cognos%20data%20collections.htm#_Toc451173027%3FTocPath%3DConfigurations%7CReal-Time%2520Data%2520Collection%7CCognos%2520Data%2520Collections%7CData%2520Collection%2520Activity%7C_____2", "parent": "Defining Real-Time Designer Settings,Configuring Real-Time Solutions Settings in Real-Time Designer,System Administration,", "version": "6.5", "rank": 6}, {"id": "DE8B01DE-CE7E-E811-801B-543C6C5B470B", "text": "Callouts", "link": "http://www.extranice.com/rts65/#../Subsystems/System_Administration/content/rt_system_admin/callouts.htm#real_time_optimization_settings_961635260_1289857%3FTocPath%3DConfigurations%7CSystem%2520Administration%7CConfiguring%2520Real-Time%2520Solutions%2520Settings%2520in%2520Real-Time%2520Designer%7CDefining%2520Real-Time%2520Designer%2520Settings%7C_____2", "parent": "Defining Real-Time Designer Settings,Configuring Real-Time Solutions Settings in Real-Time Designer,System Administration,", "version": "6.5", "rank": 6}, {"id": "DA68F9E3-CE7E-E811-801B-543C6C5B470B", "text": "Callouts", "link": "http://www.extranice.com/rts64/#../Subsystems/New%20Online%20Engage/content/collecting%20and%20viewing%20data%20in%20cognos%20quick%20guide%20draft8/cognos%20data%20collections.htm#_Toc451173027%3FTocPath%3DConfigurations%7CReal-Time%2520Data%2520Collection%7CCognos%2520Data%2520Collections%7CData%2520Collection%2520Activity%7C_____2", "parent": "Defining Real-Time Designer Settings,Configuring Real-Time Solutions Settings in Real-Time Designer,System Administration,", "version": "6.4", "rank": 6}]}
    - action_suggest
    - utter_ask_didthathelp
* deny
    - utter_ack_findalternatives
    - utter_ask_version
* question
    - utter_ask_details
* question{"keywords": "using the reports to analyze the cause for spikes in productivity"}
    - slot{"keywords": "using the reports to analyze the cause for spikes in productivity"}
    - action_search
    - slot{"matches": [{"id": "8E8D01DE-CE7E-E811-801B-543C6C5B470B", "text": "Use the Reports to Analyze the Cause for Spikes in Productivity", "link": "http://www.extranice.com/rts65/#../Subsystems/RTAM_Solution/content/rtam_user_guide/use%20the%20reports%20to%20analyze%20the%20cause%20for%20spikes%20in%20productivity.htm#rtam_best_practices_3277801691_1569312%3FTocPath%3DSolution%2520Deployments%7CRTAM%2520(Real-Time%2520Activity%2520Monitoring)%2520Solution%7CRTAM%2520Best%2520Practices%7CPerform%2520Routine%2520RTAM%2520Activities%7C_____1", "parent": "Perform Routine RTAM Activities,RTAM Best Practices,RTAM (Real-Time Activity Monitoring) Solution,", "version": "6.5", "rank": 9}, {"id": "30A97803-CF7E-E811-801B-543C6C5B470B", "text": "Use the Reports to Analyze the Cause for Spikes in Productivity", "link": "http://www.extranice.com/rts65/#../Subsystems/RTAM_Solution/content/rtam_user_guide/use%20the%20reports%20to%20analyze%20the%20cause%20for%20spikes%20in%20productivity.htm#rtam_best_practices_3277801691_1569312%3FTocPath%3DSolution%2520Deployments%7CRTAM%2520(Real-Time%2520Activity%2520Monitoring)%2520Solution%7CRTAM%2520Best%2520Practices%7CPerform%2520Routine%2520RTAM%2520Activities%7C_____1", "parent": "Perform Routine RTAM Activities,RTAM Best Practices,RTAM (Real-Time Activity Monitoring) Solution,", "version": "6.5", "rank": 9}, {"id": "10C4F08C-CF7E-E811-801B-543C6C5B470B", "text": "Use the Reports to Analyze the Cause for Spikes in Productivity", "link": "http://www.extranice.com/rts66/#../Subsystems/DesktopAnalytics_Solution/content/rtam_user_guide/use%20the%20reports%20to%20analyze%20the%20cause%20for%20spikes%20in%20productivity.htm#rtam_best_practices_3277801691_1569312%3FTocPath%3DSolution%2520Deployments%7CDesktop%2520Analytics%2520Solution%7CDesktop%2520Analytics%2520Best%2520Practices%7CPerform%2520Routine%2520Desktop%2520Analytics%2520Activities%7C_____1", "parent": "Perform Routine RTAM Activities,RTAM Best Practices,RTAM (Real-Time Activity Monitoring) Solution,", "version": "6.6", "rank": 9}]}
    - action_suggest
    - utter_ask_didthathelp
* affirm
    - utter_thanks
    - utter_anything_else
* thanks
    - utter_goodbye
    - action_restart

## Generated Story 308663065766999905
* greet
    - utter_greet
* question{"product": "apa"}
    - slot{"product": "apa"}
    - utter_product_page
* affirm
    - utter_thanks
    - utter_ask_howcanhelp
* question{"keywords": "assign a solution to a team?"}
    - slot{"keywords": "assign a solution to a team?"}
    - action_search
    - action_suggest
    - utter_ask_didthathelp
* deny
    - utter_ack_findalternatives
    - utter_ask_version
* inform{"version": "6.5"}
    - slot{"version": "6.5"}
    - utter_ask_details
* question{"keywords": "manually assigning solution to a team"}
    - slot{"keywords": "manually assigning solution to a team"}
    - action_search
    - action_suggest
    - utter_ask_didthathelp
* thanks
    - utter_thanks
    - utter_anything_else
* deny
    - utter_goodbye
    - action_restart

## Generated Story -5243216725232933346
* question
    - utter_greet
* question{"keywords": "how the weather is going to be in pune today?"}
    - slot{"keywords": "how the weather is going to be in pune today?"}
    - action_search
    - action_suggest
* deny
    - utter_ask_details
* question{"keywords": "manually assigning solution to a team"}
    - slot{"keywords": "manually assigning solution to a team"}
    - utter_ask_product
* inform{product:"apa"}
    - slot{product:"apa"}
    - action_search
    - action_suggest
    - utter_ask_didthathelp
* affirm
    - utter_thanks
* goodbye
    - utter_goodbye
    - export