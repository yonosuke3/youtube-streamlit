import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('DataFrame')


st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!!'

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')


st.write('expander')
expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')



df = pd.DataFrame({
    '1列目': [1,2,3,4],
    '2列目': [10,20,30,40]
})

st.write(df)

st.dataframe(df, width=100,height=100)

st.dataframe(df.style.highlight_max(axis=0))

st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項

```python
バッククォートは@の上のキー
import streamlit as st
import numpy as np
import pandas as pd
```


"""


df2 = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)

st.write(df2)

st.line_chart(df2)

st.area_chart(df2)

st.bar_chart(df2)



df3 = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
st.map(df3)



st.write('インタラクティブなウィジット３つ')


st.write('１ チェックボックス')
if st.checkbox('Show Image'):
    img = Image.open('sample.jpg')
    st.image(img,caption='heya sample', use_column_width=True)



st.write('2 セレクトボックス')
option = st.selectbox(
    'あなたが好きな数字を教えてください。',
    list(range(1,11))
)
'あなたの好きな数字は、',option, 'です。'



st.write('３ テキスト入力')
option1 = st.sidebar.text_input('あなたの趣味を教えてください。')
'あなたの趣味は',option1,'です'


st.write('4 スライダー')
condition = st.slider('あなたの今の調子は？',0, 100, 50)
'コンデション:',condition



