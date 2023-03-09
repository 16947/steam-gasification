import streamlit as st
import pickle
import pandas as pd
from pandas import DataFrame
import pickle

st.title("生物质蒸汽气化案例")
model = pickle.load(open("H21.dat","rb"))




with st.form('user_input'):
    # ash
    A = st.number_input(
        label = "灰分含量(A)",
        min_value = 0.00,max_value=50.00)
    # ② FC
    FC= st.number_input(
        label = "固定碳含量 (FC) ",
        min_value = 0.00,max_value=30.00)
    # ③VM
    V= st.number_input(
        label = "挥发分含量 (V) ",
        min_value = 0.00,max_value=90.00)
    # ③C
    C = st.number_input(
        label = "碳元素含量 (C) ",key=1,
        min_value = 0.00,max_value=60.00)
    # ③C
    H= st.number_input(
        label = "氢元素含量 (H) ",
        min_value =0.00,max_value=10.00)
    # ② FC
    O= st.number_input(
        label = "氧元素含量 (O) ",
        min_value = 0.00,max_value=50.00)
    # ③C
    ER = st.number_input(
        label = "氧气当量比 (ER) ",
        min_value = 0.00,max_value=0.5)
    # ⑤ T
    T = st.number_input(
        label = "反应温度(T)",
        min_value = 600,max_value=1000
    )
    # ⑥SB
    SB= st.number_input(
        label = "生物质与水蒸气质量比(S/B) ",
        min_value = 0.00,max_value=5.00
    )
    # 提交按钮
    submitted = st.form_submit_button('提交: 进行产气含量预测')
    #if submitted:
        #st.write("### 用户输入的特征数据：{}".format([A, FC, V, C, H, O, ER, T, SB]))


        # 将所有特征合并起来
    temp_feature = [(A, FC, V, C, H, O, ER, T, SB)]
    data_frame = DataFrame(temp_feature,index=None,columns = ['A', 'FC', 'V', 'C', 'H', 'O', 'ER', 'T', 'SB'])
        # 模型预测
    new_prediction = model.predict(data_frame)

        # 预测的企鹅类别
        #predict_species = label_names[new_prediction][0]

        # 根据模型的特征重要性输出，绘制特征：bill length, bill depth, flipper length 的直方图
    st.subheader("预测的组分含量是：{}  %".format(new_prediction))
