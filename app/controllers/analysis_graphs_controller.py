import pandas as pd
from flask import Blueprint, jsonify
from flask import Response
import matplotlib.pyplot as plt
from io import BytesIO
from app.repo.psql_repo.analysis_queries_1 import deadliest_attack_types, get_top_5_damage_targets
from app.repo.psql_repo.analysis_queries_2 import groups_that_attacked_targets_frequently, cooperation_between_groups
import seaborn as sns

analysis_graphs_blueprint = Blueprint("analysis_graphs", __name__)

# שאלה 1
@analysis_graphs_blueprint.route('/attack_types', methods=['GET'])
def attack_types_graph():
    data = deadliest_attack_types()

    labels = [item['attacktype'] for item in data]
    values = [item['total_damage'] for item in data]

    plt.figure(figsize=(10, 6))
    plt.bar(labels, values)
    plt.title('Deadliest Attack Types')
    plt.xlabel('Attack Type')
    plt.ylabel('Total Damage')
    plt.xticks(rotation=45, ha='right')

    buf = BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png')
    buf.seek(0)

    return Response(buf.getvalue(), mimetype='image/png')

# שאלה 3
@analysis_graphs_blueprint.route('/damage-targets', methods=['GET'])
def damage_targets_graph():
    data = get_top_5_damage_targets()

    labels = [item['targettype_txt'] for item in data]
    values = [item['total_damage'] for item in data]

    plt.figure(figsize=(10, 6))
    plt.bar(labels, values)
    plt.title('Top 5 Damage Targets')
    plt.xlabel('Target Type')
    plt.ylabel('Total Damage')
    plt.xticks(rotation=45, ha='right')

    buf = BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png')
    buf.seek(0)

    return Response(buf.getvalue(), mimetype='image/png')

# שאלה 13
@analysis_graphs_blueprint.route('/cooperation_between_groups', methods=['GET'])
def cooperation_between_groups_route():
    try:
        res = cooperation_between_groups()
        return jsonify(res), 200
    except Exception as e:
        error = str(e)
        print(error)
        return jsonify({'error': error}), 501


# שאלה 15
@analysis_graphs_blueprint.route('/groups-frequent-targets', methods=['GET'])
def frequent_targets_graph():
    data = groups_that_attacked_targets_frequently()

    df = pd.DataFrame(data)

    pivot = df.pivot(index='group_name', columns='target_type', values='attack_count').fillna(0)

    plt.figure(figsize=(12, 8))
    sns.heatmap(pivot, annot=True, fmt=".0f", cmap="coolwarm", cbar_kws={'label': 'Attack Count'})
    plt.title("Attack Counts by Group and Target Type")
    plt.xlabel("Target Type")
    plt.ylabel("Group Name")
    plt.tight_layout()

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    return Response(buf.getvalue(), mimetype='image/png')
