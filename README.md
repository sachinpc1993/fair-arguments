# Evaluating Fairness in Argument Retrieval

Existing commercial search engines often struggle to represent different perspectives of a search query. Argument retrieval systems address this limitation of search engines and provide both positive (PRO) and negative (CON) perspectives about a user's information need on a controversial topic (e.g., climate change). The effectiveness of such argument retrieval systems is typically evaluated based on topical relevance and argument quality, without taking into account the often differing number of documents shown for the argument stances (PRO or CON). Therefore, systems may retrieve relevant passages, but with a biased exposure of arguments. In this work, we analyze a range of non-stochastic fairness-aware ranking and diversity metrics to evaluate the extent to which argument stances are fairly exposed in argument retrieval systems.

Using the official runs of the argument retrieval task Ttouché at CLEF 2020, as well as synthetic data to control the amount and order of argument stances in the rankings, we show that systems with the best effectiveness in terms of topical relevance are not necessarily the most fair or the most diverse in terms of argument stance. The relationships we found between (un)fairness and diversity metrics shed light on how to evaluate group fairness -- in addition to topical relevance -- in argument retrieval settings.

# Input file structure format

- **topic** : topic number.
- **stance** : stance of the argument PRO/CON.
- **id** : document id.
- **rank** : rank position.
- **score** : As provided by the retriever.
- **group_name** : Group name (can be any name provided by the participants of the evaluation campaign).
- **system_name** : System name (can be any name provided by the participants of the evaluation campaign).
- **protected_group** : The stance which has the minimum representation for the topic.
- **pro_count** : The number of PRO stances for the topic in qrel.
- **con_count** : The number of CON stances for the topic in qrel.

Save the input file as **_input_file.csv_** in the same folder and the main.py.

# How to Run

The code in the **_main.py_** file shows how to use the unfairness evaluation functions.

`python main.py`

Output file **_System_Unfairness.csv_** will be generated in the same folder as the **_main.py_**


# Citation

Sachin Pathiyan Cherumanal, Damiano Spina, Falk Scholer, and W. Bruce Croft. 2021. Evaluating Fairness in Argument Retrieval. In Proceedings of the 30th ACM International Conference on Information & Knowledge Management (CIKM '21). Association for Computing Machinery, New York, NY, USA, 3363–3367. DOI:https://doi.org/10.1145/3459637.3482099

```bibtex
@inproceedings{10.1145/3459637.3482099,
author = {Pathiyan Cherumanal, Sachin and Spina, Damiano and Scholer, Falk and Croft, W. Bruce},
title = {Evaluating Fairness in Argument Retrieval},
year = {2021},
isbn = {9781450384469},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3459637.3482099},
doi = {10.1145/3459637.3482099},
abstract = {Existing commercial search engines often struggle to represent different perspectives
of a search query. Argument retrieval systems address this limitation of search engines
and provide both positive (PRO) and negative (CON) perspectives about a user's information
need on a controversial topic (e.g., climate change). The effectiveness of such argument
retrieval systems is typically evaluated based on topical relevance and argument quality,
without taking into account the often differing number of documents shown for the
argument stances (PRO or CON). Therefore, systems may retrieve relevant passages,
but with a biased exposure of arguments. In this work, we analyze a range of non-stochastic
fairness-aware ranking and diversity metrics to evaluate the extent to which argument
stances are fairly exposed in argument retrieval systems.Using the official runs of
the argument retrieval task Ttouch\'{e} at CLEF 2020, as well as synthetic data to control
the amount and order of argument stances in the rankings, we show that systems with
the best effectiveness in terms of topical relevance are not necessarily the most
fair or the most diverse in terms of argument stance. The relationships we found between
(un)fairness and diversity metrics shed light on how to evaluate group fairness --
in addition to topical relevance -- in argument retrieval settings.},
booktitle = {Proceedings of the 30th ACM International Conference on Information &amp; Knowledge Management},
pages = {3363–3367},
numpages = {5},
keywords = {evaluation, fairness, argument retrieval},
location = {Virtual Event, Queensland, Australia},
series = {CIKM '21}
}
```
