## Generated Story 385444109151785804
* greet
    - utter_greet
    - utter_ask_howcanhelp
* inform{"keywords": "updating the agent binaries?"}
    - slot{"keywords": "updating the agent binaries?"}
    - utter_ask_product
* question{"version": "1"}
    - slot{"version": "1"}
    - utter_ask_product
* inform
* question{"keywords": "real-time solutions"}
    - slot{"keywords": "real-time solutions"}
    - action_search
    - slot{"matches": 777}
    - action_suggest
* thankyou
    - utter_thanks
    - export