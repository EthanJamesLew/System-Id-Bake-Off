import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


from app.fetch_data import SysidApiClient


client = SysidApiClient("http://127.0.0.1:8000")


def _get_model(mid, l):
    for li in l:
        if li.id == mid:
            return li


# system name lookup
syslu = {s.id: s.name for s in client.systemid_methods}


### Make Streamlit Website
st.title("System Identification Bake Off")


### Build Benchmarks Section
st.header("Benchmarks")

benches, bdims, bidims = list(
    zip(*[(b.name, b.dims, b.input_dims) for b in client.benchmarks])
)

data = pd.DataFrame(
    {
        "Dimensions": np.array(bdims + bidims),
        "Type": np.array(["State"] * len(bdims) + ["Input"] * len(bidims)),
        "Benchmark": np.array(benches * 2),
    }
)

selector = alt.selection_single(encodings=["x", "color"])
bar_chart = (
    alt.Chart(data)
    .mark_bar()
    .encode(
        x=alt.X(f"sum(Dimensions)"),
        y=alt.Y("Benchmark", sort="-x"),
        color=alt.condition(selector, "Type", alt.value("lightgray")),
    )
    .add_selection(selector)
)
st.altair_chart(bar_chart, use_container_width=True)


### Build Scores Section
st.header("Scores")
for bres in client.results:
    for sres in bres:
        if len(sres) > 0:
            score = _get_model(
                sres[0].value.score, client.scores
            )  # slu[sres[0].value.score]
            benchmark = _get_model(
                sres[0].benchmark, client.benchmarks
            )  # blu[sres[0].benchmark]

            st.subheader(f"{benchmark.name}")
            st.text(f"{benchmark.descr}")
            vals, sysname = list(zip(*[(v.value.value, syslu[v.method]) for v in sres]))

            data = pd.DataFrame(
                {score.name: np.array(vals), "Methods": np.array(sysname)}
            )

            bar_chart = (
                alt.Chart(data)
                .mark_bar()
                .encode(
                    x=alt.X(f"{score.name}", scale=alt.Scale(type="log")),
                    y=alt.Y(
                        "Methods", sort=("-" if not score.lower_better else "") + "x"
                    ),
                )
            )
            st.altair_chart(bar_chart, use_container_width=True)
