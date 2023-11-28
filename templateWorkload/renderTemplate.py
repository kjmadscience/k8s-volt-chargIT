import argparse
import os
import yaml
from jinja2 import Environment, FileSystemLoader

def render_template(template_file, context):
    env = Environment(loader=FileSystemLoader(os.path.dirname(template_file)), autoescape=True)
    template = env.get_template(os.path.basename(template_file))
    rendered_output = template.render(context)
    rendered_data = yaml.safe_load(rendered_output)
    return rendered_data

def save_rendered_yaml(rendered_data, output_file):
    with open(output_file, "w") as file:
        yaml.dump(rendered_data, file, default_flow_style=False)

def parse_arguments():
    parser = argparse.ArgumentParser(description='Render Jinja template and save as YAML. Example command with values:\n\n'
                                     'python3 renderTemplate.py \\\n'
                                     '  --hostnames "custom-hostname" \\\n'
                                     '  --recordcount "10000000" \\\n'
                                     '  --load_data_tpms "50" \\\n'
                                     '  --maxinitialcredit "10000" \\\n'
                                     '  --tpms "35" \\\n'
                                     '  --durationseconds "120" \\\n'
                                     '  --queryseconds "5" \\\n'
                                     '  --kv_tpms "20" \\\n'
                                     '  --kv_durationseconds "100" \\\n'
                                     '  --kv_queryseconds "30" \\\n'
                                     '  --kv_jsonsize "1024" \\\n'
                                     '  --kv_deltaproportion "1" \\\n'
                                     '  --kafkaserverplusport "kafka:9092" \\\n'
                                     '  --kafka_recordcount "300" \\\n'
                                     '  --kafka_tpms "3" \\\n'
                                     '  --kafka_durationseconds "300" \\\n'
                                     '  --kafka_max_amount "500" \\\n',
                                     formatter_class=argparse.RawTextHelpFormatter)
    # Add all variables from configMap with default=None
    parser.add_argument('--hostnames', default=None, help='Specify hostnames value')
    parser.add_argument('--recordcount', default=None, help='Specify kafkaHostnames value')
    parser.add_argument('--load_data_tpms', default=None, help='Specify userCount value')
    parser.add_argument('--maxinitialcredit', default=None, help='Specify tpMs value')
    parser.add_argument('--tpms', default=None, help='Specify durationSeconds value')
    parser.add_argument('--durationseconds', default=None, help='Specify missingRatio value')
    parser.add_argument('--queryseconds', default=None, help='Specify dupRatio value')
    parser.add_argument('--kv_tpms', default=None, help='Specify lateRatio value')
    parser.add_argument('--kv_durationseconds', default=None, help='Specify dateis1970Ratio value')
    parser.add_argument('--kv_queryseconds', default=None, help='Specify offset value')
    parser.add_argument('--kv_jsonsize', default=None, help='Specify userkafkaflag value')
    parser.add_argument('--kv_deltaproportion', default=None, help='Specify kafkaPort value')
    parser.add_argument('--kafkaserverplusport', default=None, help='Specify maxActiveSessions value')
    parser.add_argument('--kafka_recordcount', default=None, help='Specify maxActiveSessions value')
    parser.add_argument('--kafka_tpms', default=None, help='Specify maxActiveSessions value')
    parser.add_argument('--kafka_durationseconds', default=None, help='Specify maxActiveSessions value')
    parser.add_argument('--kafka_max_amount', default=None, help='Specify maxActiveSessions value')
    

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()

    # Assuming the template file is in the same directory as the script
    template_file_path = "configMap.j2"
    output_file_path = "rendered_configMap.yaml"

    template_context = vars(args)

    rendered_data = render_template(template_file_path, template_context)
    save_rendered_yaml(rendered_data, output_file_path)

    print(f"Rendered YAML saved to {output_file_path}")
