import pandas as pd
from utils import *
from tqdm import tqdm
import regex
import traceback
from sentence_transformers import SentenceTransformer, util
import argparse
import os

os.environ["TOKENIZERS_PARALLELISM"] = "false"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--deployment_name",
        type=str,
        help="model to run topic generation with ('gpt-4', 'gpt-35-turbo', 'mistral-7b-instruct)",
    )
    parser.add_argument(
        "--max_tokens", type=int, default=500, help="max tokens to generate"
    )
    parser.add_argument(
        "--temperature", type=float, default=0.0, help="temperature for generation"
    )
    parser.add_argument("--top_p", type=float, default=0.0, help="top-p for generation")
    parser.add_argument(
        "--data",
        type=str,
        default="data/input/sample.jsonl",
        help="data to run generation on",
    )
    parser.add_argument(
        "--prompt_file",
        type=str,
        default="prompt/generation_1.txt",
        help="file to read prompts from",
    )
    parser.add_argument(
        "--seed_file",
        type=str,
        default="prompt/seed_1.md",
        help="markdown file to read the seed topics from",
    )
    parser.add_argument(
        "--out_file",
        type=str,
        default="data/output/generation_1.jsonl",
        help="file to write results to",
    )
    parser.add_argument(
        "--topic_file",
        type=str,
        default="data/output/generation_1.md",
        help="file to write topics to",
    )
    parser.add_argument(
        "--verbose", type=bool, default=False, help="whether to print out results"
    )
    args = parser.parse_args()

    # 打印 args.data 的类型和内容
    print(f"args.data 的类型：{type(args.data)}")
    print(f"args.data 的内容：{args.data}")

    # 检查文件是否存在
    if not os.path.exists(args.data):
        print(f"文件 {args.data} 不存在，请检查文件路径。")
        return
    else:
        print(f"文件 {args.data} 存在，正在读取。")

    # 尝试读取数据
    try:
        df = pd.read_json(args.data, lines=True, encoding='utf-8')
        print("数据读取成功。")
        print("数据框的前几行：")
        print(df.head())
    except ValueError as e:
        print(f"读取 JSON 数据时发生 ValueError：{e}")
        return
    except Exception as e:
        print(f"读取 JSON 数据时发生未知错误：{e}")
        return

    # ...（后续的代码）

if __name__ == "__main__":
    main()
