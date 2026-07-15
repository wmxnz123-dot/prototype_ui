import os

filepath = '/Users/zhanghuimin/Downloads/00数据沙箱/prototype_ui/developer_nav.js'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 删除 message top nav
content = content.replace(
    "    { id: 'help', label: '帮助中心', href: 'help_center.html?nav=help' },\n    { id: 'message', label: '消息中心', href: 'my_messages.html?nav=my-messages' }\n];",
    "    { id: 'help', label: '帮助中心', href: 'help_center.html?nav=help' }\n];"
)

# 替换 monitor 和 删除 message side nav
old_side = """    monitor: [
        { type: 'link', label: '调用告警', href: 'call_alarm.html?nav=monitor-call', navKey: 'monitor-call' },
        { type: 'link', label: '配额告警', href: 'quota_alarm.html?nav=monitor-quota', navKey: 'monitor-quota' }
    ],
    help: [
        { type: 'link', label: '帮助中心', href: 'help_center.html?nav=help', navKey: 'help' }
    ],
    message: [
        { type: 'link', label: '我的消息', href: 'my_messages.html?nav=my-messages', navKey: 'my-messages' },
        { type: 'link', label: '告警消息', href: 'alert_messages.html?nav=alert-messages', navKey: 'alert-messages' }
    ]
};"""

new_side = """    monitor: [
        { type: 'link', label: '数据源监控', href: '', navKey: 'monitor-datasource', disabled: true },
        {
            type: 'group',
            label: '资源监控',
            children: [
                { type: 'link', label: '调用告警', href: 'call_alarm.html?nav=monitor-call', navKey: 'monitor-call' }
            ]
        },
        { type: 'link', label: '模型监控', href: '', navKey: 'monitor-model', disabled: true },
        { type: 'link', label: '配额告警', href: 'quota_alarm.html?nav=monitor-quota', navKey: 'monitor-quota' }
    ],
    help: [
        { type: 'link', label: '帮助中心', href: 'help_center.html?nav=help', navKey: 'help' }
    ]
};"""

content = content.replace(old_side, new_side)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Nav updated successfully.")
