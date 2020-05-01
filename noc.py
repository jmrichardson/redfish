from kafka import KafkaConsumer
import json
import pandas as pd
import streamlit as st
import datetime

def _max_width_():
    max_width_str = f"max-width: 2000px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )

_max_width_()

topics = ['tampa-collector', 'tampa-listener', 'tampa-utilities', 'tampa-n3000', 'tampa-logs']
consumer = KafkaConsumer(group_id=None, bootstrap_servers=['kafka:9092'])
# consumer = KafkaConsumer(group_id=None, auto_offset_reset='earliest', bootstrap_servers=['kafka:9092'])
consumer.subscribe(topics)

rows = 5

'''
## Health Status
Kafka Topic: **tampa-collector**
'''
cols = ['TimeStamp', 'Processors', 'Memory', 'Storage', 'Temperatures', 'Network', 'PowerSupplies', 'Fans']
collector_df = pd.DataFrame(columns=cols)
collector_st = st.empty()

'''
## Alerts
Kafka Topic: **tampa-listener**
'''
cols = ['TimeStamp', 'EventType', 'Severity', 'MessageId', 'MessageArg']
listener_df = pd.DataFrame(columns=cols)
listener_st = st.empty()

'''
## Logs
Kafka Topic: **tampa-logs**
'''
cols = ['TimeStamp', 'Path', 'Message']
logs_df = pd.DataFrame(columns=cols)
logs_st = st.empty()

'''
## Utilities
Kafka Topic: **tampa-utilities**
'''
cols = ['TimeStamp', 'Command', 'Message']
utilities_df = pd.DataFrame(columns=cols)
utilities_st = st.empty()


for msg in consumer:

    if msg.topic == 'tampa-collector':
        js = json.loads(msg[6])
        df = pd.DataFrame([{
            'TimeStamp': datetime.datetime.fromtimestamp(msg.timestamp/1000).strftime('%Y-%m-%d %H:%M:%S'),
            'Processors': js['Oem']['Hpe']['AggregateHealthStatus']['Processors']['Status']['Health'],
            'Memory': js['Oem']['Hpe']['AggregateHealthStatus']['Memory']['Status']['Health'],
            'Storage': js['Oem']['Hpe']['AggregateHealthStatus']['Storage']['Status']['Health'],
            'Temperatures': js['Oem']['Hpe']['AggregateHealthStatus']['Temperatures']['Status']['Health'],
            'Network': js['Oem']['Hpe']['AggregateHealthStatus']['Network']['Status']['Health'],
            'PowerSupplies': js['Oem']['Hpe']['AggregateHealthStatus']['PowerSupplies']['Status']['Health'],
            'Fans': js['Oem']['Hpe']['AggregateHealthStatus']['Fans']['Status']['Health'],
        }])
        collector_df = collector_df.append(df).sort_values("TimeStamp", ascending=False).reset_index(drop=True).iloc[:rows, :]
        collector_st.table(collector_df)

    if msg.topic == 'tampa-listener':
        js = json.loads(msg[6])
        df = pd.DataFrame([{
            'TimeStamp': datetime.datetime.fromtimestamp(msg.timestamp/1000).strftime('%Y-%m-%d %H:%M:%S'),
            'EventType': js['Events'][0]['EventType'],
            'Severity': js['Events'][0]['Severity'],
            'MessageId': js['Events'][0]['MessageId'],
            'MessageArg': js['Events'][0]['MessageArgs'][0],
        }])
        listener_df = listener_df.append(df).sort_values("TimeStamp", ascending=False).reset_index(drop=True).iloc[:rows, :]
        listener_st.table(listener_df)

    if msg.topic == 'tampa-logs':
        js = json.loads(msg[6])
        df = pd.DataFrame([{
            'TimeStamp': datetime.datetime.fromtimestamp(msg.timestamp/1000).strftime('%Y-%m-%d %H:%M:%S'),
            'Path': js['path'],
            'Message': js['message'],
        }])
        logs_df = logs_df.append(df).sort_values("TimeStamp", ascending=False).reset_index(drop=True).iloc[:rows, :]
        logs_st.table(logs_df)

    if msg.topic == 'tampa-utilities':
        js = json.loads(msg[6])
        df = pd.DataFrame([{
            'TimeStamp': datetime.datetime.fromtimestamp(msg.timestamp/1000).strftime('%Y-%m-%d %H:%M:%S'),
            'Command': js['command'],
            'Message': js['message'],
        }])
        utilities_df = utilities_df.append(df).sort_values("TimeStamp", ascending=False).reset_index(drop=True).iloc[:rows, :]
        utilities_st.table(utilities_df)





