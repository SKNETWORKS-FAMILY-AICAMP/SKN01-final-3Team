import argparse

import logging
import os
import sys

from camel.typing import ModelType
from chatdev.chat_chain import ChatChain

root = os.path.dirname(__file__)
sys.path.append(root)
from dotenv import load_dotenv

load_dotenv()


class Runner:
    def run(self, *args, **kwargs):

        def get_config(company):
            config_dir = os.path.join(root, "CompanyConfig", company)
            default_config_dir = os.path.join(root, "CompanyConfig", "Default")

            config_files = [
                "ChatChainConfig.json",
                "PhaseConfig.json",
                "RoleConfig.json",
            ]

            config_paths = []

            for config_file in config_files:
                company_config_path = os.path.join(config_dir, config_file)
                default_config_path = os.path.join(default_config_dir, config_file)

                if os.path.exists(company_config_path):
                    config_paths.append(company_config_path)
                else:
                    config_paths.append(default_config_path)

            return tuple(config_paths)

        config_path, config_phase_path, config_role_path = get_config(kwargs['config'])
        chat_chain = ChatChain(
            model_name=kwargs['model_name'],
            user_token=kwargs['user_token'],
            base_url=kwargs['base_url'],
            config_path=config_path,
            config_phase_path=config_phase_path,
            config_role_path=config_role_path,
            task_prompt=kwargs['task'],
            project_name=kwargs['project'],
            org_name='SI-Follow',
            model_type=ModelType.OLLAMA,
            code_path="",
        )
        logging.basicConfig(
            filename=chat_chain.log_filepath,
            level=logging.INFO,
            format="[%(asctime)s %(levelname)s] %(message)s",
            datefmt="%Y-%d-%m %H:%M:%S",
            encoding="utf-8",
        )
        chat_chain.pre_processing()
        chat_chain.make_recruitment()
        chat_chain.execute_chain()
        chat_chain.post_processing()

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--task', default="develop a simple calculator app", help='define task to develop with agents')
parser.add_argument('-u', '--user_token', default="test_user", help='to use different root dir by user')
parser.add_argument('-n', '--project_name', default="test_project", help="define project name")
parser.add_argument('-c', '--config', default='Default', help='config to develop project')
parser.add_argument('-m', '--model_name', default='llama3.2', help='model name: [llama3.1, llama3.2]')
parser.add_argument('--api_url', default="https://si-follow.loca.lt", help="llm api url")


if __name__ == "__main__":
    args = parser.parse_args()
    
    runner = Runner()
    runner.run(
        task=args.task,
        user_token=args.user_token,
        project=args.project_name,
        config=args.config,
        model_name=args.model_name,
        base_url=args.api_url
        )