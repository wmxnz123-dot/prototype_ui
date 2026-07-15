const developerTopNavItems = [
    { id: 'workbench', label: '开发工作台', href: 'index.html' },
    { id: 'resource', label: '资源中心', href: 'data_source_manage.html?nav=resource-source' },
    { id: 'sandbox', label: '数据沙箱', href: 'scene_center.html?nav=sandbox-task' },
    { id: 'model', label: '数据模型', href: 'image_repo_manage.html?nav=result-repo' },
    { id: 'approval', label: '审批中心', href: 'data_resource_apply.html?nav=initiated-resource' },
    { id: 'monitor', label: '监控中心', href: 'call_alarm.html?nav=monitor-call' },
    { id: 'help', label: '帮助中心', href: 'help_center.html?nav=help' }
];

const developerSideNavMap = {
    workbench: [
        { type: 'link', label: '开发工作台', href: 'index.html', navKey: 'workbench-home', icon: 'fa-desktop' },
        { type: 'link', label: '管理工作台', href: 'admin_workbench.html', navKey: 'workbench-admin', icon: 'fa-chart-line' }
    ],
    resource: [
        {
            type: 'group',
            label: '数据资源接入',
            icon: 'fa-plug',
            children: [
                { type: 'link', label: '数据源管理', href: 'data_source_manage.html?nav=resource-source', navKey: 'resource-source' },
                { type: 'link', label: '对外数据发布', href: '', navKey: 'resource-publish', disabled: true },
                { type: 'link', label: '对外数据分类', href: '', navKey: 'resource-category', disabled: true },
                { type: 'link', label: '自用数据管理', href: 'own_data_manage.html?nav=resource-own', navKey: 'resource-own' }
            ]
        },
        {
            type: 'group',
            label: '数据资源申请',
            icon: 'fa-file-signature',
            children: [
                { type: 'link', label: '资源超市', href: 'resource_supermarket.html?nav=resource-market', navKey: 'resource-market' },
                { type: 'link', label: '已申请数据资源', href: 'applied_data_resources.html?nav=resource-applied', navKey: 'resource-applied' }
            ]
        },
        {
            type: 'group',
            label: '数据资源授权',
            icon: 'fa-key',
            children: [
                { type: 'link', label: '已授权数据资源', href: 'authorized_data_resources.html?nav=resource-authorized', navKey: 'resource-authorized' }
            ]
        }
    ],
    sandbox: [
        {
            type: 'group',
            label: '配额管理',
            icon: 'fa-chart-pie',
            children: [
                { type: 'link', label: '总配额管理', href: '', navKey: 'sandbox-quota-total', disabled: true },
                { type: 'link', label: '部门配额管理', href: '', navKey: 'sandbox-quota-dept', disabled: true }
            ]
        },
        {
            type: 'group',
            label: '正式区',
            icon: 'fa-server',
            children: [
                { type: 'link', label: '沙箱容器监控', href: '', navKey: 'sandbox-prod-container1', disabled: true },
                { type: 'link', label: '空间集群监控', href: '', navKey: 'sandbox-prod-cluster', disabled: true },
                { type: 'link', label: '沙箱容器监控', href: '', navKey: 'sandbox-prod-container2', disabled: true },
                { type: 'link', label: '库表授权管理', href: '', navKey: 'sandbox-prod-auth', disabled: true }
            ]
        },
        {
            type: 'group',
            label: '测试区',
            icon: 'fa-vial',
            children: [
                { type: 'link', label: '测试区使用说明', href: '', navKey: 'sandbox-test-doc', disabled: true },
                { type: 'link', label: '库表权限查看', href: '', navKey: 'sandbox-test-auth', disabled: true },
                { type: 'link', label: '库表资源查看', href: '', navKey: 'sandbox-test-resource-db', disabled: true },
                { type: 'link', label: '接口资源查看', href: '', navKey: 'sandbox-test-resource-api', disabled: true }
            ]
        },
        { type: 'link', label: '开发任务', href: 'scene_center.html?nav=sandbox-task', navKey: 'sandbox-task', icon: 'fa-tasks' }
    ],
    model: [
        {
            type: 'group',
            label: '开发成果管理',
            icon: 'fa-code-branch',
            children: [
                { type: 'link', label: '镜像仓库管理', href: 'image_repo_manage.html?nav=result-repo', navKey: 'result-repo' },
                { type: 'link', label: '镜像上传', href: 'image_upload.html?nav=result-upload', navKey: 'result-upload' },
                { type: 'link', label: 'API列表', href: 'api_list.html?nav=result-api', navKey: 'result-api' }
            ]
        },
        {
            type: 'group',
            label: '模型管理',
            icon: 'fa-cube',
            children: [
                { type: 'link', label: '模型注册', href: 'model_deploy_list.html?nav=model-register', navKey: 'model-register' },
                { type: 'link', label: '已注册模型', href: 'deployed_model_list.html?nav=model-registered', navKey: 'model-registered' }
            ]
        },
        {
                            type: 'group',
                            label: '模型申请',
                            icon: 'fa-paper-plane',
                            children: [
                                { type: 'link', label: '模型超市', href: 'model_market.html?nav=model-market', navKey: 'model-market' },
                                { type: 'link', label: '已申请模型', href: 'model_applied.html?nav=model-applied', navKey: 'model-applied' }
                            ]
                        },
                        {
                            type: 'group',
                            label: '模型授权',
                            icon: 'fa-key',
                            children: [
                                { type: 'link', label: '已授权模型', href: 'model_authorized.html?nav=model-authorized', navKey: 'model-authorized' }
                            ]
                        }
    ],
    approval: [
        {
            type: 'group',
            label: '已发起',
            icon: 'fa-paper-plane',
            children: [
                { type: 'link', label: '数据资源申请工单', href: 'data_resource_apply.html?nav=initiated-resource', navKey: 'initiated-resource' },
                { type: 'link', label: '数据资源续期工单', href: 'data_resource_renew.html?nav=initiated-renew', navKey: 'initiated-renew' },
                { type: 'link', label: '模型部署申请工单', href: 'model_deploy_work_order.html?nav=initiated-deploy', navKey: 'initiated-deploy' },
                { type: 'link', label: '模型变更申请工单', href: 'model_change_work_order.html?nav=initiated-change', navKey: 'initiated-change' },
                { type: 'link', label: '模型申请工单', href: 'model_apply_work_order.html?nav=initiated-model-apply', navKey: 'initiated-model-apply' }
            ]
        },
        {
            type: 'group',
            label: '待处理',
            icon: 'fa-clock',
            children: [
                { type: 'link', label: '数据资源审核', href: 'data_resource_audit.html?nav=pending-resource', navKey: 'pending-resource' },
                { type: 'link', label: '数据续期审核', href: 'data_resource_renew_audit.html?nav=pending-renew', navKey: 'pending-renew' },
                { type: 'link', label: '模型注册部署', href: 'model_deploy_audit.html?nav=pending-deploy', navKey: 'pending-deploy' },
                { type: 'link', label: '模型变更部署', href: 'model_change_audit.html?nav=pending-change', navKey: 'pending-change' },
                { type: 'link', label: '模型申请审核', href: 'model_apply_audit.html?nav=pending-model-apply', navKey: 'pending-model-apply' }
            ]
        }
    ],
    monitor: [
        { type: 'link', label: '数据源监控', href: '', navKey: 'monitor-datasource', disabled: true, icon: 'fa-database' },
        {
            type: 'group',
            label: '资源监控',
            icon: 'fa-desktop',
            children: [
                { type: 'link', label: '调用告警', href: 'call_alarm.html?nav=monitor-call', navKey: 'monitor-call' }
            ]
        },
        { type: 'link', label: '模型监控', href: '', navKey: 'monitor-model', disabled: true, icon: 'fa-chart-line' },
        { type: 'link', label: '配额告警', href: 'quota_alarm.html?nav=monitor-quota', navKey: 'monitor-quota', icon: 'fa-bell' }
    ],
    help: [
        { type: 'link', label: '帮助中心', href: 'help_center.html?nav=help', navKey: 'help', icon: 'fa-circle-question' }
    ]
};

const developerPathDefaults = {
    'index.html': { group: 'workbench', navKey: 'workbench-home' },
    'admin_workbench.html': { group: 'workbench', navKey: 'workbench-admin' },
    'data_resources.html': { group: 'sandbox', navKey: 'sandbox-quota' },
    'own_data_manage.html': { group: 'resource', navKey: 'resource-own' },
    'own_data_manage_add.html': { group: 'resource', navKey: 'resource-own' },
    'own_data_manage_add_step2.html': { group: 'resource', navKey: 'resource-own' },
    'resource_supermarket.html': { group: 'resource', navKey: 'resource-market' },
    'resource_supermarket_detail.html': { group: 'resource', navKey: 'resource-market' },
    'applied_data_resources.html': { group: 'resource', navKey: 'resource-applied' },
    'authorized_data_resources.html': { group: 'resource', navKey: 'resource-authorized' },
    'data_source_manage.html': { group: 'resource', navKey: 'resource-source' },
    'data_resource_apply.html': { group: 'approval', navKey: 'initiated-resource' },
    'scene_center.html': { group: 'sandbox', navKey: 'sandbox-task' },
    'scene_detail.html': { group: 'sandbox', navKey: 'sandbox-quota' },
    'dev_team.html': { group: 'sandbox', navKey: 'sandbox-test' },
    'dev_task_create.html': { group: 'sandbox', navKey: 'sandbox-task' },
    'image_repo_manage.html': { group: 'model', navKey: 'result-repo' },
    'image_upload.html': { group: 'model', navKey: 'result-upload' },
    'api_list.html': { group: 'model', navKey: 'result-api' },
    'model_deploy_list.html': { group: 'model', navKey: 'model-register' },
    'model_deploy_add.html': { group: 'model', navKey: 'model-register' },
    'model_deploy_add_step2.html': { group: 'model', navKey: 'model-register' },
    'model_deploy_add_step3.html': { group: 'model', navKey: 'model-register' },
    'deployed_model_list.html': { group: 'model', navKey: 'model-registered' },
    'model_deploy_work_order.html': { group: 'approval', navKey: 'initiated-deploy' },
    'model_change_work_order.html': { group: 'approval', navKey: 'initiated-change' },
    'resource_alert.html': { group: 'monitor', navKey: 'monitor-call' },
    'call_alarm.html': { group: 'monitor', navKey: 'monitor-call' },
    'quota_alarm.html': { group: 'monitor', navKey: 'monitor-quota' },
    'help_center.html': { group: 'help', navKey: 'help' },
    'data_resource_audit.html': { group: 'approval', navKey: 'pending-resource' },
    'data_resource_renew.html': { group: 'approval', navKey: 'initiated-renew' },
    'data_resource_renew_audit.html': { group: 'approval', navKey: 'pending-renew' },
    'model_deploy_audit.html': { group: 'approval', navKey: 'pending-deploy' },
    'model_change_audit.html': { group: 'approval', navKey: 'pending-change' },
    'model_apply_work_order.html': { group: 'approval', navKey: 'initiated-model-apply' },
    'model_apply_audit.html': { group: 'approval', navKey: 'pending-model-apply' },
    'model_change_record.html': { group: 'model', navKey: 'model-market' },
    'offline_model_list.html': { group: 'model', navKey: 'model-registered' },
    'capability_pack_list.html': { group: 'model', navKey: 'model-market' },
    'model_market.html': { group: 'model', navKey: 'model-market' },
    'model_applied.html': { group: 'model', navKey: 'model-applied' },
    'model_authorized.html': { group: 'model', navKey: 'model-authorized' }
};

const developerNavKeyToGroup = {};

Object.keys(developerSideNavMap).forEach((groupId) => {
    developerSideNavMap[groupId].forEach((item) => {
        if (item.type === 'group') {
            item.children.forEach((child) => {
                developerNavKeyToGroup[child.navKey] = groupId;
            });
            return;
        }
        developerNavKeyToGroup[item.navKey] = groupId;
    });
});

function getDeveloperNavState() {
    const url = new URL(window.location.href);
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    const currentNav = url.searchParams.get('nav');
    const fallback = developerPathDefaults[currentPath] || developerPathDefaults['index.html'];
    const activeGroup = currentNav ? (developerNavKeyToGroup[currentNav] || fallback.group) : fallback.group;
    const activeNav = currentNav || fallback.navKey;

    return {
        currentPath,
        activeGroup,
        activeNav
    };
}

function renderDeveloperTopNav(state) {
    const legacyContainer = document.getElementById('developer-top-nav');
    if (legacyContainer) {
        legacyContainer.classList.add('hidden');
    }

    const header = document.querySelector('body > header');
    if (!header || !header.firstElementChild || !header.lastElementChild) {
        return;
    }

    const headerLeft = header.firstElementChild;
    const headerRight = header.lastElementChild;

    header.classList.remove('justify-between');
    header.classList.add('gap-6');
    headerLeft.classList.add('flex-1', 'min-w-0');
    headerRight.classList.add('shrink-0');

    let container = document.getElementById('developer-header-top-nav');
    if (!container) {
        container = document.createElement('div');
        container.id = 'developer-header-top-nav';
        container.className = 'ml-8 flex items-center gap-2 overflow-x-auto whitespace-nowrap';
        headerLeft.appendChild(container);
    }

    container.innerHTML = developerTopNavItems.map((item) => {
        const isActive = item.id === state.activeGroup;
        return `
            <a
                href="${item.href}"
                class="px-4 h-[34px] inline-flex items-center rounded-md border transition-colors whitespace-nowrap text-[14px] ${
                    isActive
                        ? 'bg-white/18 border-white/30 text-white font-medium shadow-sm'
                        : 'border-transparent text-white/80 hover:text-white hover:bg-white/10'
                }"
            >
                ${item.label}
            </a>
        `;
    }).join('');
}

window.toggleNavGroup = function(groupId) {
    const content = document.getElementById(`nav-group-content-${groupId}`);
    const arrow = document.getElementById(`nav-group-arrow-${groupId}`);
    if (content.classList.contains('hidden')) {
        content.classList.remove('hidden');
        arrow.classList.remove('fa-angle-right');
        arrow.classList.add('fa-angle-down');
    } else {
        content.classList.add('hidden');
        arrow.classList.remove('fa-angle-down');
        arrow.classList.add('fa-angle-right');
    }
};

function renderDeveloperNavItem(item, state, isChild = false) {
    const isActive = item.navKey === state.activeNav;
    const paddingClass = isChild ? 'pl-11 pr-4 py-2.5' : 'px-4 py-3';
    const textClass = isChild ? 'text-[13px]' : 'text-[14px] font-medium';
    
    const iconHtml = !isChild && item.icon ? `<i class="fa-solid ${item.icon} w-5 text-center mr-2 text-lg"></i>` : '';

    if (item.disabled) {
        return `
            <div
                class="flex items-center ${paddingClass} text-[#c0c4cc] cursor-not-allowed transition-colors rounded-lg mx-2 my-0.5"
                title="暂无页面"
            >
                ${iconHtml}
                <span>${item.label}</span>
            </div>
        `;
    }

    return `
        <a
            href="${item.href}"
            class="flex items-center ${paddingClass} transition-colors rounded-lg mx-2 my-0.5 ${
                isActive
                    ? 'bg-blue-50 text-[#1c7ffd]'
                    : 'text-[#606266] hover:text-[#1c7ffd] hover:bg-gray-50'
            } ${textClass}"
        >
            ${iconHtml}
            <span>${item.label}</span>
        </a>
    `;
}

function renderDeveloperSideNav(state) {
    const container = document.getElementById('developer-side-nav');
    if (!container) {
        return;
    }

    const sections = developerSideNavMap[state.activeGroup] || [];

    container.innerHTML = `
        <div class="flex flex-col py-2">
            ${sections.map((item, index) => {
                if (item.type === 'group') {
                    const groupActive = item.children.some((child) => child.navKey === state.activeNav);
                    const groupId = `group-${index}`;
                    
                    return `
                        <div class="flex flex-col mb-1">
                            <div 
                                class="flex items-center justify-between px-4 py-3 mx-2 rounded-lg cursor-pointer transition-colors ${groupActive ? 'text-[#1c7ffd]' : 'text-[#303133] hover:bg-gray-50'} font-medium text-[14px]"
                                onclick="toggleNavGroup('${groupId}')"
                            >
                                <div class="flex items-center">
                                    <i class="fa-solid ${item.icon || 'fa-folder'} w-5 text-center mr-2 text-lg"></i>
                                    <span>${item.label}</span>
                                </div>
                                <i id="nav-group-arrow-${groupId}" class="fa-solid ${groupActive ? 'fa-angle-down' : 'fa-angle-right'} text-gray-400 text-xs transition-transform duration-200"></i>
                            </div>
                            <div id="nav-group-content-${groupId}" class="flex flex-col mt-0.5 ${groupActive ? '' : 'hidden'}">
                                ${item.children.map((child) => renderDeveloperNavItem(child, state, true)).join('')}
                            </div>
                        </div>
                    `;
                }
                return `<div class="mb-1">${renderDeveloperNavItem(item, state, false)}</div>`;
            }).join('')}
        </div>
    `;
}

document.addEventListener('DOMContentLoaded', () => {
    try {
        const state = getDeveloperNavState();
        renderDeveloperTopNav(state);
        renderDeveloperSideNav(state);
    } catch (e) {
        document.body.innerHTML += '<div style="color:red;z-index:9999;position:fixed;top:0;left:0;background:white;padding:20px;">' + e.toString() + ' ' + e.stack + '</div>';
    }
});
