import os

filepath = '/Users/zhanghuimin/Downloads/00数据沙箱/prototype_ui/developer_nav.js'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 替换 Top Nav 的 href
old_top_nav = "{ id: 'monitor', label: '监控中心', href: 'resource_alert.html?nav=monitor' }"
new_top_nav = "{ id: 'monitor', label: '监控中心', href: 'call_alarm.html?nav=monitor-call' }"
content = content.replace(old_top_nav, new_top_nav)

# 替换 Side Nav Map 的 monitor 节点
old_side_nav = """    monitor: [
        { type: 'link', label: '监控中心', href: 'resource_alert.html?nav=monitor', navKey: 'monitor' }
    ],"""
new_side_nav = """    monitor: [
        { type: 'link', label: '调用告警', href: 'call_alarm.html?nav=monitor-call', navKey: 'monitor-call' },
        { type: 'link', label: '配额告警', href: 'quota_alarm.html?nav=monitor-quota', navKey: 'monitor-quota' }
    ],"""
content = content.replace(old_side_nav, new_side_nav)

# 替换 defaults
old_defaults = """    'resource_alert.html': { group: 'monitor', navKey: 'monitor' },"""
new_defaults = """    'resource_alert.html': { group: 'monitor', navKey: 'monitor' },
    'call_alarm.html': { group: 'monitor', navKey: 'monitor-call' },
    'quota_alarm.html': { group: 'monitor', navKey: 'monitor-quota' },"""
content = content.replace(old_defaults, new_defaults)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Navigation fixed successfully.")
