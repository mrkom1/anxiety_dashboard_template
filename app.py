import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def indicator(label: str, score: int):
    fig = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
        value=score,
    mode = "gauge+number",
    title = {'text': label},
    gauge = {'axis': {'range': [None, 100]},
             'steps' : [
                 {'range': [0, 20], 'color': "#7ABCF3"},
                 {'range': [20, 40], 'color': "#8298F0"},
                 {'range': [40, score], 'color': "#8D68EA"},
                 {'range': [score, 80], 'color': "lightgray"},
                 {'range': [80, 100], 'color': "lightgray"}],
             'threshold' : {'line': {'color': "red", 'width': 4}, 
                            'thickness': 0.75, 'value': score}}))
    return fig


def FAV_chart():
    df = pd.DataFrame({'name':['low', 'normal', 'average', 'moderate', 'high',],
                   'value':[110, 10, 10, 10, 60],
                   'x':[0, 0, 0, 0, 0]  })

    fig = px.bar(df,
                 title="Fast Attention Variability (FAV):",
                 x='value',
                 y='x',
                 color='name',
                 orientation='h',
                 color_discrete_sequence=["#7ABCF3", "#8298F0", 
                                          "#8D68EA", "#C392C9", 
                                          "#D6A0BD"])

    fig.add_shape(type="line",
        x0=126, y0=-0.15, x1=126, y1=0.2,
        line=dict(
            color="#B284D5",
            width=1.5,
        ))

    fig.add_annotation(x=126, y=0.2,
                text="126ms",
                showarrow=False,
                font=dict(
                    color="#B284D5",
                    size=24,
                ),
                yshift=20)

    fig.update_yaxes(showticklabels=False, title=None)
    fig.update_xaxes(range=[100, 150], title=None)
    fig.update_traces(width=.3,
                    hovertemplate='level: ')
    fig.update_layout(
        showlegend=False,
        barmode='stack',
        autosize=False,
        width=700,
        height=300,
        template="plotly_white",
        xaxis_tickmode="array",
        xaxis_tickvals=[100, 110, 120, 130, 140, 150],
        xaxis_ticktext=['...', '110ms', '120ms', '130ms', '140ms', '...'],
    )

    return fig


def AAT_chart():
    df = pd.DataFrame({'name':['normal', 'high',],
                   'value':[10, 20],
                   'x':[0, 0]  })

    fig = px.bar(df,
                 title="Avoidance Attention Threshold (AAT):",
                 x='value',
                 y='x',
                 color='name',
                 orientation='h',
                 color_discrete_sequence=["#D6A0BD", "#8298F0"])
    
    fig.add_shape(type="line",
        x0=7, y0=-0.15, x1=7, y1=0.2,
        line=dict(
            color="#B284D5",
            width=1.5,
        ))

    fig.add_annotation(x=7, y=0.2,
                text="7",
                showarrow=False,
                font=dict(
                    color="#B284D5",
                    size=24,
                ),
                yshift=20)

    fig.update_yaxes(showticklabels=False, title=None)
    fig.update_xaxes(range=[3, 20], title=None)
    fig.update_traces(width=.3,
                      hovertemplate='level: ')
    fig.update_layout(
        showlegend=False,
        barmode='stack',
        autosize=False,
        width=700,
        height=300,
        template="plotly_white",
        xaxis_tickmode="array",
        xaxis_tickvals=[3, 10, 20],
        xaxis_ticktext=['...', '10', '...'],
    )
    return fig


def AB_chart():
    df = pd.DataFrame({'name':['low', 'normal', 'average', 'moderate', 'high',],
                   'value':[370, 30, 30, 30, 60],
                   'x':[0, 0, 0, 0, 0]  })

    fig = px.bar(df,
                 title="Attention Bias (AB):",
                 x='value',
                 y='x',
                 color='name',
                 orientation='h',
                 color_discrete_sequence=["#7ABCF3", "#8298F0", 
                                          "#8D68EA", "#C392C9", 
                                          "#D6A0BD"])

    fig.add_shape(type="line",
        x0=420, y0=-0.15, x1=420, y1=0.2,
        line=dict(
            color="#B284D5",
            width=1.5,
        ))

    fig.add_annotation(x=420, y=0.2,
                text="420ms",
                showarrow=False,
                font=dict(
                    color="#B284D5",
                    size=24,
                ),
                yshift=20)

    fig.update_yaxes(showticklabels=False, title=None)
    fig.update_xaxes(range=[340, 490], title=None)
    fig.update_traces(width=.3,
                    hovertemplate='level: ')
    fig.update_layout(
        showlegend=False,
        barmode='stack',
        autosize=False,
        width=700,
        height=300,
        template="plotly_white",
        xaxis_tickmode="array",
        xaxis_tickvals=[340, 370, 400, 430, 460, 490],
        xaxis_ticktext=['...', '370ms', '400ms', '430ms', '460ms', '...'],
    )

    return fig


def gad_7_chart():
    df = pd.DataFrame({'name':['low', 'below average', 'moderate', 'high',],
                   'value':[4, 5, 5, 7],
                   'x':[0, 0, 0, 0]  })

    fig = px.bar(df,
                 title="GAD-7:",
                 x='value',
                 y='x',
                 color='name',
                 orientation='h',
                 color_discrete_sequence=["#7ABCF3", "#8298F0", 
                                          "#C392C9", "#D6A0BD"])

    fig.add_shape(type="line",
        x0=10, y0=-0.15, x1=10, y1=0.2,
        line=dict(
            color="#B284D5",
            width=1.5,
        ))

    fig.add_annotation(x=10, y=0.2,
                text="10",
                showarrow=False,
                font=dict(
                    color="#B284D5",
                    size=24,
                ),
                yshift=20)

    fig.update_yaxes(showticklabels=False, title=None)
    fig.update_xaxes(range=[0, 21], title=None)
    fig.update_traces(width=.3,
                    hovertemplate='level: ')
    fig.update_layout(
        showlegend=False,
        barmode='stack',
        autosize=False,
        width=700,
        height=300,
        template="plotly_white",
        xaxis_tickmode="array",
        xaxis_tickvals=[0, 4, 9, 14, 21],
        xaxis_ticktext=[' ', '4', '9', '14', '21', ' ']
    )

    return fig


def stai_chart():
    df = pd.DataFrame({'name': ['low', 'moderate', 'high', ],
                       'value': [30, 15, 20],
                       'x': [0, 0, 0]})

    fig = px.bar(df,
                 title="State-Trait Anxiety Inventory :",
                 x='value',
                 y='x',
                 color='name',
                 orientation='h',
                 color_discrete_sequence=["#7ABCF3", "#8D68EA",
                                          "#D6A0BD"])

    fig.add_shape(type="line",
                  x0=25, y0=-0.15, x1=25, y1=0.2,
                  line=dict(
                      color="#B284D5",
                      width=1.5,
                  ))

    fig.add_annotation(x=25, y=0.2,
                       text="25",
                       showarrow=False,
                       font=dict(
                           color="#B284D5",
                           size=24,
                       ),
                       yshift=20)

    fig.update_yaxes(showticklabels=False, title=None)
    fig.update_xaxes(range=[5, 65], title=None)
    fig.update_traces(width=.3,
                      hovertemplate='level: ')
    fig.update_layout(
        showlegend=False,
        barmode='stack',
        autosize=False,
        width=700,
        height=300,
        template="plotly_white",
        xaxis_tickmode="array",
        xaxis_tickvals=[5, 30, 45, 65],
        xaxis_ticktext=[' ', '30', '45', ' ']
    )

    return fig


if __name__ == '__main__':
    st.set_page_config(layout="wide")
    col1, col2 = st.columns(2)

    col1.plotly_chart(indicator(label="Attention Behavior Score:",
                score=30), use_column_width=True)
    col1.write("The Attention Behavior Score (ABS) is a measure used to assess "
            "an individual's attentional abilities. The ABS is a composite "
            "score, which can be calculated by combining multiple measures "
            "of attention. The ABS is not a standardized measure, and "
            "different studies may use different methods for calculating the "
            "score. The ABS is generally used to understand the cognitive "
            "functioning of an individual in order to inform interventions "
            "and treatment.")
    with col1.expander("More"):
        st.plotly_chart(AB_chart(), use_column_width=True)
        st.markdown(
            '<p style="font-size: 20px;"> AAB score: <span style="color:#8769E2;">Average</span></p>',
            unsafe_allow_html=True)
        st.write("Attentional bias refers to the phenomenon where an individual's "
                "attention is preferentially directed toward certain stimuli or "
                "types of information. This can occur due to a variety of "
                "factors, including past experiences, emotions, and cognitive "
                "biases. For example, if an individual has a fear of spiders, "
                "they may show an attentional bias towards pictures of spiders, "
                "devoting more attention to them than to other stimuli. "
                "Attentional bias can have a significant impact on an "
                "individual's behavior, thoughts, and emotions, and has been "
                "studied in a variety of contexts, including mental health, "
                "addiction, and decision-making.")

        st.plotly_chart(FAV_chart(), use_column_width=True)
        st.markdown(
            '<p style="font-size: 20px;"> FAV score: <span style="color:#8769E2;">Average</span></p>',
        unsafe_allow_html=True)
        st.write("Fast Attention Variability (FAV) is a term used in the field of "
                "cognitive psychology to describe the tendency for an individual "
                "to quickly shift their attention between different stimuli in "
                "their environment. Individuals with high FAV are thought to have "
                "a greater alertness and, accordingly, this may signal greater "
                "anxiety.")

        st.plotly_chart(AAT_chart(), use_column_width=True)
        st.markdown(
            '<p style="font-size: 20px;"> AAT score: <span style="color:#CEA1BC;">Normal</span></p>',
            unsafe_allow_html=True)
        st.write("Avoidance Attention Threshold is related to the concept of "
                "avoidance behavior, which is a type of behavior that is used "
                "to avoid an aversive or unpleasant stimulus. In the field of "
                "psychology and psychiatry, avoidance behavior is often "
                "associated with anxiety disorders and phobias, and is "
                "considered as a maladaptive form of coping.")


    col2.plotly_chart(indicator(label="Subjective Anxiety Score:",
                                score=55), use_column_width=True)
    col2.write("The Subjective Anxiety Score (SAS) is a measure used to assess "
                "an individual's level of anxiety. The SAS is typically "
                "self-reported and can be assessed through the use of "
                "standardized questionnaires. These questionnaires typically "
                "include a series of statements or questions related to "
                "anxiety symptoms, such as nervousness, worry or fear, and "
                "individuals are asked to rate their level of agreement with "
                "each statement.")
    with col2.expander("More"):
        st.plotly_chart(gad_7_chart(), use_column_width=True)
        st.markdown(
            '<p style="font-size: 20px;"> GAD-7 score: <span style="color:#BC94C6;">Moderate</span></p>',
    unsafe_allow_html=True)
        st.write("The GAD-7 (Generalized Anxiety Disorder 7-item scale) is a "
               "widely used self-report questionnaire that assesses symptoms "
               "of generalized anxiety disorder (GAD) in adults. GAD is a "
               "psychiatric disorder characterized by excessive, "
               "uncontrollable worry and anxiety about multiple events or "
               "activities. The GAD-7 was developed to provide a quick and "
               "easy way to screen for GAD in primary care and other settings.")
        
        st.plotly_chart(stai_chart(), use_column_width=True)
        st.markdown(
        '<p style="font-size: 20px;"> STAI score: <span style="color:#89BAEE;">Low</span></p>',
        unsafe_allow_html=True)
        st.write('The State-Trait Anxiety Inventory (STAI) is a widely used '
                'self-report questionnaire that assesses symptoms of anxiety. '
                'It was developed by Charles D. Spielberger in the 1970s and '
                'consists of two separate 20-item scales, the "State Anxiety '
                'Scale" and the "Trait Anxiety Scale". The Trait scale measures '
                'an individuals general tendency to experience anxiety, it '
                'assesses feelings of apprehension, tension, nervousness, and '
                'worry that are relatively stable across different situations '
                'and contexts. The items on the Trait scale are also rated on a '
                '4-point Likert scale, with responses ranging from "almost '
                'never" to "almost always".')

    st.title("Recomendations")
    st.write("Dealing with anxiety can be challenging, but there are several things you can do to manage your symptoms. Here are some tips that may be helpful:")
    st.write("1. Practice relaxation techniques: Relaxation techniques such as deep breathing, progressive muscle relaxation, and yoga can help reduce physical symptoms of anxiety, such as rapid heart rate and muscle tension.")
    st.write("2. Engage in regular physical activity: Regular exercise can help reduce anxiety symptoms by releasing endorphins, which are chemicals in the brain that act as natural painkillers and mood elevators.")
    st.write("3. Get enough sleep: Adequate sleep is essential for good mental health. Try to get 7-8 hours of sleep each night, and establish a regular sleep schedule.")
    st.write("4. Challenge negative thoughts: Anxiety often involves negative thoughts or catastrophic thinking. Try to challenge these thoughts and replace them with more balanced and realistic thoughts.")
    st.write("5. Seek professional help: If your anxiety is interfering with your daily life, consider seeking help from a mental health professional. They can help you identify triggers for your anxiety and develop coping strategies.")
    st.write("6. Try cognitive-behavioral therapy (CBT): CBT is a form of therapy that can help you change the way you think about and respond to situations that trigger your anxiety.")
    st.write("7. Try Medications: If the above methods are not working, your doctor may suggest medications, such as antidepressants or anti-anxiety medications, to help you manage your symptoms.")
    st.write("Remember that it is important to be patient and persistent when working on managing anxiety. It may take some time to find the right approach or combination of approaches that work best for you.")
