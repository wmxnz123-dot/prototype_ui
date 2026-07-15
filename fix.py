with open("scene_center.html", "w") as f:
    f.write(r"""<!DOCTYPE html>
<html lang=\"zh-CN\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>数据沙箱平台 - 开发任务</title>
    <script src=\"https://cdn.tailwindcss.com\"></script>
    <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css\">
    <style>
        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: #d1d5db; border-radius: 3px; }
        ::-webkit-scrollbar-thumb:hover { background: #9ca3af; }
        body { font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, \"Helvetica Neue\", Arial, sans-serif; }
    </style>
</head>
<body class=\"h-screen w-screen flex flex-col overflow-hidden bg-[#f0f2f5] text-[14px] text-gray-700\">
    <header class=\"h-14 bg-[#1c7ffd] flex justify-between items-center px-6 text-white shrink-0 shadow-sm z-10\">
        <div class=\"flex items-center gap-2\">
            <i class=\"fa-solid fa-cubes-stacked text-2xl\"></i>
            <span class=\"text-lg font-medium tracking-wider ml-1\">数据沙箱平台</span>
        </div>
        <div class=\"flex items-center gap-6\">
            <div class=\"relative cursor-pointer hover:text-gray-200 transition-colors\" onclick=\"window.location.href='my_messages.html'\">
                <i class=\"fa-regular fa-bell text-xl\"></i>
                <span class=\"absolute -top-1.5 -right-2 bg-red-500 text-white text-[10px] font-bold px-1.5 py-0.5 rounded-full border border-[#1c7ffd] leading-none\">20</span>
            </div>
            <div class=\"flex items-center gap-2 cursor-pointer hover:text-gray-200 transition-colors\">
                <img src=\"https://api.dicebear.com/7.x/avataaars/svg?seed=yiyun&backgroundColor=b6e3f4\" alt=\"avatar\" class=\"w-8 h-8 rounded-full border border-blue-300 bg-white\">
                <span>yiyun</span>
            </div>
        </div>
    </header>

    <div class=\"flex-1 flex overflow-hidden\">
        <aside class=\"w-[220px] bg-white border-r border-gray-200 shrink-0 overflow-y-auto\">
            <div id=\"developer-side-nav\" class=\"py-4\"></div>
        </aside>

        <script src=\"./developer_nav.js\"></script>

        <main class=\"flex-1 flex flex-col overflow-hidden\">
            <div id=\"developer-top-nav\" class=\"h-[52px] bg-white border-b border-gray-200 px-6 flex items-center gap-2 shrink-0 overflow-x-auto\"></div>
            <div class=\"h-[52px] flex items-center px-6 text-[#606266] shrink-0 bg-transparent text-sm\">
                <span>数据沙箱</span>
                <span class=\"mx-2\">/</span>
                <span class=\"text-[#303133] font-medium\">开发任务</span>
            </div>

            <div class=\"flex-1 px-6 pb-6 flex flex-col gap-4 overflow-y-auto pr-2\">
                <div class=\"bg-white rounded-lg shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] p-5 flex justify-between items-center shrink-0\">
                    <div class=\"flex items-center gap-8\">
                        <div class=\"flex items-center gap-3\">
                            <span class=\"text-[#606266]\">任务名称：</span>
                            <input type=\"text\" placeholder=\"请输入\" class=\"border border-gray-300 rounded px-3 py-1.5 text-sm w-[220px] focus:outline-none focus:border-[#1c7ffd] transition-colors placeholder-gray-400\">
                        </div>
                        <div class=\"flex items-center gap-3\">
                            <span class=\"text-[#606266]\">任务状态：</span>
                            <div class=\"relative\">
                                <select class=\"border border-gray-300 rounded px-3 py-1.5 text-sm w-[220px] focus:outline-none focus:border-[#1c7ffd] text-gray-400 bg-white appearance-none cursor-pointer transition-colors\">
                                    <option value=\"\">请选择</option>
                                    <option value=\"1\" class=\"text-gray-700\">草稿</option>
                                    <option value=\"2\" class=\"text-gray-700\">开发中</option>
                                    <option value=\"3\" class=\"text-gray-700\">已完成</option>
                                </select>
                                <i class=\"fa-solid fa-chevron-down absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 text-xs pointer-events-none\"></i>
                            </div>
                        </div>
                    </div>
                    <div class=\"flex items-center gap-3\">
                        <button class=\"px-5 py-1.5 border border-gray-300 rounded text-[#606266] hover:text-[#1c7ffd] hover:border-[#1c7ffd] hover:bg-blue-50 transition-colors text-sm flex items-center gap-1.5 bg-white\">
                            <i class=\"fa-solid fa-rotate-right\"></i> 重置
                        </button>
                        <button class=\"px-5 py-1.5 bg-[#1c7ffd] border border-[#1c7ffd] rounded text-white hover:bg-blue-500 transition-colors text-sm flex items-center gap-1.5 shadow-sm\">
                            <i class=\"fa-solid fa-magnifying-glass\"></i> 查询
                        </button>
                    </div>
                </div>

                <div class=\"flex justify-between items-center mt-2 mb-1 px-1 shrink-0\">
                    <h3 class=\"text-[16px] font-bold text-[#303133]\">我的任务列表</h3>
                    <div class=\"text-[#606266] text-sm flex items-center gap-1.5 cursor-pointer hover:text-[#1c7ffd] transition-colors\">
                        任务开始时间 <i class=\"fa-solid fa-sort text-gray-400\"></i><span class=\"mx-2 text-gray-300\">|</span>任务截止时间 <i class=\"fa-solid fa-sort text-gray-400\"></i>
                    </div>
                </div>

                <div class=\"grid grid-cols-3 gap-5 pb-4\">
                    
                    <!-- Card 1 -->
                    <div onclick=\"openCreateTaskModal()\" class=\"group relative bg-white rounded-lg shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] border border-gray-100 overflow-hidden flex flex-col h-[210px] transition-all hover:shadow-lg hover:border-blue-200 cursor-pointer\">
                        <div class=\"absolute inset-0 bg-gradient-to-br from-[#ffffff] via-[#f0f6ff] to-[#e1edff] opacity-0 group-hover:opacity-100 transition-opacity duration-300 z-0\">
                            <svg class=\"absolute bottom-0 right-0 w-full h-full opacity-60 pointer-events-none\" viewBox=\"0 0 100 100\" preserveAspectRatio=\"none\">
                                <path d=\"M100,100 L100,40 C80,70 50,90 0,100 Z\" fill=\"rgba(64,158,255,0.06)\"></path>
                                <path d=\"M100,100 L100,0 C70,40 30,80 0,100 Z\" fill=\"rgba(64,158,255,0.04)\"></path>
                            </svg>
                        </div>
                        <div class=\"relative z-10 p-5 flex flex-col h-full items-center justify-center text-center\">
                            <div class=\"w-12 h-12 rounded-full bg-[#1c7ffd] text-white flex items-center justify-center text-xl shadow-sm mb-3\">
                                <i class=\"fa-solid fa-plus\"></i>
                            </div>
                            <span class=\"text-[#303133] font-bold text-[16px]\">新增任务入口</span>
                            <span class=\"text-[#909399] text-[13px] mt-2 leading-relaxed\">点击创建任务，选择已申请的数据资源与开发者账号，快速进入在线开发。</span>
                        </div>
                    </div>

                    <!-- Card 2 -->
                    <div class=\"group relative bg-white rounded-lg shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] border border-gray-100 overflow-hidden flex flex-col h-[210px] transition-all hover:shadow-lg hover:border-blue-200 cursor-default\">
                        <div class=\"absolute inset-0 bg-gradient-to-br from-[#ffffff] via-[#f0f6ff] to-[#e1edff] opacity-0 group-hover:opacity-100 transition-opacity duration-300 z-0\">
                            <svg class=\"absolute bottom-0 right-0 w-full h-full opacity-60 pointer-events-none\" viewBox=\"0 0 100 100\" preserveAspectRatio=\"none\">
                                <path d=\"M100,100 L100,40 C80,70 50,90 0,100 Z\" fill=\"rgba(64,158,255,0.06)\"></path>
                                <path d=\"M100,100 L100,0 C70,40 30,80 0,100 Z\" fill=\"rgba(64,158,255,0.04)\"></path>
                            </svg>
                        </div>
                        <div class=\"relative z-10 p-5 flex flex-col h-full\">
                            <div class=\"flex justify-between items-start mb-4\">
                                <div class=\"flex items-center gap-3\">
                                    <div class=\"w-11 h-11 rounded-full bg-[#1c7ffd] text-white flex items-center justify-center text-xl shadow-sm shrink-0\">
                                        <i class=\"fa-solid fa-envelope\"></i>
                                    </div>
                                    <div class=\"flex flex-col\">
                                        <span class=\"text-[#303133] font-bold text-[15px] truncate w-32\" title=\"测试离线任务...\">测试离线任务...</span>
                                        <span class=\"text-[#909399] text-[12px] mt-0.5\">任务ID：CJ20260602001</span>
                                    </div>
                                </div>
                                <div class=\"bg-[#1c7ffd] text-white px-2 py-0.5 rounded-full text-[11px] flex items-center shadow-sm whitespace-nowrap\">
                                    <i class=\"fa-solid fa-circle-check mr-1\"></i> 草稿
                                </div>
                            </div>
                            <div class=\"border-b border-gray-100 mb-3 group-hover:border-blue-100 transition-colors duration-300\"></div>
                            <div class=\"flex flex-col gap-1.5 mb-auto\">
                                <span class=\"text-[#606266] text-[13px] truncate\" title=\"任务描述：测试离线任务_20260602001\">任务描述：测试离线任务_20260602001</span>
                                <div class=\"flex items-center gap-6 text-[#909399] text-[13px] mt-1\">
                                    <span>数据资源数：3</span>
                                    <span>数据产品数：0</span>
                                    <span>公共数据产品数：0</span>
                                </div>
                            </div>
                            <div class=\"relative h-8 mt-4 overflow-hidden\">
                                <div class=\"absolute inset-0 flex items-center text-[#909399] text-[12px] transition-all duration-300 group-hover:opacity-0 group-hover:translate-y-4\">
                                    任务开始时间：2026-06-02 &nbsp;&nbsp; 任务截止时间：2026-12-31
                                </div>
                                <div class=\"absolute inset-0 flex items-center gap-2 opacity-0 translate-y-4 transition-all duration-300 group-hover:opacity-100 group-hover:translate-y-0\">
                                    <a href=\"scene_detail.html\" class=\"flex-1 text-center py-1.5 bg-white border border-gray-200 rounded text-[#606266] hover:text-[#1c7ffd] hover:border-[#1c7ffd] hover:bg-blue-50 text-[12px] transition-colors shadow-sm cursor-pointer\">任务详情</a>
                                    <button class=\"flex-1 text-center py-1.5 bg-white border border-gray-200 rounded text-[#606266] hover:text-[#1c7ffd] hover:border-[#1c7ffd] hover:bg-blue-50 text-[12px] transition-colors shadow-sm cursor-pointer\">数据资源</button>
                                    <a href=\"sql_develop.html?nav=sandbox-task\" class=\"flex-1 text-center py-1.5 bg-white border border-gray-200 rounded text-[#606266] hover:text-[#1c7ffd] hover:border-[#1c7ffd] hover:bg-blue-50 text-[12px] transition-colors shadow-sm cursor-pointer\">在线开发</a>
                                    <a href=\"dev_team.html\" class=\"flex-1 text-center py-1.5 bg-white border border-gray-200 rounded text-[#606266] hover:text-[#1c7ffd] hover:border-[#1c7ffd] hover:bg-blue-50 text-[12px] transition-colors shadow-sm cursor-pointer\">开发者</a>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Card 3 -->
                    <div class=\"group relative bg-white rounded-lg shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] border border-gray-100 overflow-hidden flex flex-col h-[210px] transition-all hover:shadow-lg hover:border-blue-200 cursor-default\">
                        <div class=\"absolute inset-0 bg-gradient-to-br from-[#ffffff] via-[#f0f6ff] to-[#e1edff] opacity-0 group-hover:opacity-100 transition-opacity duration-300 z-0\">
                            <svg class=\"absolute bottom-0 right-0 w-full h-full opacity-60 pointer-events-none\" viewBox=\"0 0 100 100\" preserveAspectRatio=\"none\">
                                <path d=\"M100,100 L100,40 C80,70 50,90 0,100 Z\" fill=\"rgba(64,158,255,0.06)\"></path>
                                <path d=\"M100,100 L100,0 C70,40 30,80 0,100 Z\" fill=\"rgba(64,158,255,0.04)\"></path>
                            </svg>
                        </div>
                        <div class=\"relative z-10 p-5 flex flex-col h-full\">
                            <div class=\"flex justify-between items-start mb-4\">
                                <div class=\"flex items-center gap-3\">
                                    <div class=\"w-11 h-11 rounded-full bg-[#1c7ffd] text-white flex items-center justify-center text-xl shadow-sm shrink-0\">
                                        <i class=\"fa-solid fa-envelope\"></i>
                                    </div>
                                    <div class=\"flex flex-col\">
                                        <span class=\"text-[#303133] font-bold text-[15px] truncate w-32\" title=\"测试离线任务...\">测试离线任务...</span>
                                        <span class=\"text-[#909399] text-[12px] mt-0.5\">任务ID：CJ20260521003</span>
                                    </div>
                                </div>
                                <div class=\"bg-[#1c7ffd] text-white px-2 py-0.5 rounded-full text-[11px] flex items-center shadow-sm whitespace-nowrap\">
                                    <i class=\"fa-solid fa-circle-check mr-1\"></i> 开发中
                                </div>
                            </div>
                            <div class=\"border-b border-gray-100 mb-3 group-hover:border-blue-100 transition-colors duration-300\"></div>
                            <div class=\"flex flex-col gap-1.5 mb-auto\">
                                <span class=\"text-[#606266] text-[13px] truncate\" title=\"任务描述：测试离线任务_20260521003\">任务描述：测试离线任务_20260521003</span>
                                <div class=\"flex items-center gap-6 text-[#909399] text-[13px] mt-1\">
                                    <span>数据资源数：3</span>
                                    <span>数据产品数：0</span>
                                    <span>公共数据产品数：0</span>
                                </div>
                            </div>
                            <div class=\"relative h-8 mt-4 overflow-hidden\">
                                <div class=\"absolute inset-0 flex items-center text-[#909399] text-[12px] transition-all duration-300 group-hover:opacity-0 group-hover:translate-y-4\">
                                    任务开始时间：2026-05-21 &nbsp;&nbsp; 任务截止时间：2026-12-31
                                </div>
                                <div class=\"absolute inset-0 flex items-center gap-2 opacity-0 translate-y-4 transition-all duration-300 group-hover:opacity-100 group-hover:translate-y-0\">
                                    <a href=\"scene_detail.html\" class=\"flex-1 text-center py-1.5 bg-white border border-gray-200 rounded text-[#606266] hover:text-[#1c7ffd] hover:border-[#1c7ffd] hover:bg-blue-50 text-[12px] transition-colors shadow-sm cursor-pointer\">任务详情</a>
                                    <button class=\"flex-1 text-center py-1.5 bg-white border border-gray-200 rounded text-[#606266] hover:text-[#1c7ffd] hover:border-[#1c7ffd] hover:bg-blue-50 text-[12px] transition-colors shadow-sm cursor-pointer\">数据资源</button>
                                    <a href=\"sql_develop.html?nav=sandbox-task\" class=\"flex-1 text-center py-1.5 bg-white border border-gray-200 rounded text-[#606266] hover:text-[#1c7ffd] hover:border-[#1c7ffd] hover:bg-blue-50 text-[12px] transition-colors shadow-sm cursor-pointer\">在线开发</a>
                                    <a href=\"dev_team.html\" class=\"flex-1 text-center py-1.5 bg-white border border-gray-200 rounded text-[#606266] hover:text-[#1c7ffd] hover:border-[#1c7ffd] hover:bg-blue-50 text-[12px] transition-colors shadow-sm cursor-pointer\">开发者</a>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Card 4 -->
                    <div class=\"group relative bg-white rounded-lg shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] border border-gray-100 overflow-hidden flex flex-col h-[210px] transition-all hover:shadow-lg hover:border-blue-200 cursor-default\">
                        <div class=\"absolute inset-0 bg-gradient-to-br from-[#ffffff] via-[#f0f6ff] to-[#e1edff] opacity-0 group-hover:opacity-100 transition-opacity duration-300 z-0\">
                            <svg class=\"absolute bottom-0 right-0 w-full h-full opacity-60 pointer-events-none\" viewBox=\"0 0 100 100\" preserveAspectRatio=\"none\">
                                <path d=\"M100,100 L100,40 C80,70 50,90 0,100 Z\" fill=\"rgba(64,158,255,0.06)\"></path>
                                <path d=\"M100,100 L100,0 C70,40 30,80 0,100 Z\" fill=\"rgba(64,158,255,0.04)\"></path>
                            </svg>
                        </div>
                        <div class=\"relative z-10 p-5 flex flex-col h-full\">
                            <div class=\"flex justify-between items-start mb-4\">
                                <div class=\"flex items-center gap-3\">
                                    <div class=\"w-11 h-11 rounded-full bg-[#1c7ffd] text-white flex items-center justify-center text-xl shadow-sm shrink-0\">
                                        <i class=\"fa-solid fa-envelope\"></i>
                                    </div>
                                    <div class=\"flex flex-col\">
                                        <span class=\"text-[#303133] font-bold text-[15px] truncate w-32\" title=\"测试离线任务...\">测试离线任务...</span>
                                        <span class=\"text-[#909399] text-[12px] mt-0.5\">任务ID：CJ20260521002</span>
                                    </div>
                                </div>
                                <div class=\"bg-[#1c7ffd] text-white px-2 py-0.5 rounded-full text-[11px] flex items-center shadow-sm whitespace-nowrap\">
                                    <i class=\"fa-solid fa-circle-check mr-1\"></i> 已完成
                                </div>
                            </div>
                            <div class=\"border-b border-gray-100 mb-3 group-hover:border-blue-100 transition-colors duration-300\"></div>
                            <div class=\"flex flex-col gap-1.5 mb-auto\">
                                <span class=\"text-[#606266] text-[13px] truncate\" title=\"任务描述：测试离线任务_20260521002\">任务描述：测试离线任务_20260521002</span>
                                <div class=\"flex items-center gap-6 text-[#909399] text-[13px] mt-1\">
                                    <span>数据资源数：3</span>
                                    <span>数据产品数：0</span>
                                    <span>公共数据产品数：0</span>
                                </div>
                            </div>
                            <div class=\"relative h-8 mt-4 overflow-hidden\">
                                <div class=\"absolute inset-0 flex items-center text-[#909399] text-[12px] transition-all duration-300 group-hover:opacity-0 group-hover:translate-y-4\">
                                    任务开始时间：2026-05-21 &nbsp;&nbsp; 任务截止时间：2026-12-31
                                </div>
                                <div class=\"absolute inset-0 flex items-center gap-2 opacity-0 translate-y-4 transition-all duration-300 group-hover:opacity-100 group-hover:translate-y-0\">
                                    <a href=\"scene_detail.html\" class=\"flex-1 text-center py-1.5 bg-white border border-gray-200 rounded text-[#606266] hover:text-[#1c7ffd] hover:border-[#1c7ffd] hover:bg-blue-50 text-[12px] transition-colors shadow-sm cursor-pointer\">任务详情</a>
                                    <button class=\"flex-1 text-center py-1.5 bg-white border border-gray-200 rounded text-[#606266] hover:text-[#1c7ffd] hover:border-[#1c7ffd] hover:bg-blue-50 text-[12px] transition-colors shadow-sm cursor-pointer\">数据资源</button>
                                    <a href=\"sql_develop.html?nav=sandbox-task\" class=\"flex-1 text-center py-1.5 bg-white border border-gray-200 rounded text-[#606266] hover:text-[#1c7ffd] hover:border-[#1c7ffd] hover:bg-blue-50 text-[12px] transition-colors shadow-sm cursor-pointer\">在线开发</a>
                                    <a href=\"dev_team.html\" class=\"flex-1 text-center py-1.5 bg-white border border-gray-200 rounded text-[#606266] hover:text-[#1c7ffd] hover:border-[#1c7ffd] hover:bg-blue-50 text-[12px] transition-colors shadow-sm cursor-pointer\">开发者</a>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Card 5 -->
                    <div class=\"group relative bg-white rounded-lg shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] border border-gray-100 overflow-hidden flex flex-col h-[210px] transition-all hover:shadow-lg hover:border-blue-200 cursor-default\">
                        <div class=\"absolute inset-0 bg-gradient-to-br from-[#ffffff] via-[#f0f6ff] to-[#e1edff] opacity-0 group-hover:opacity-100 transition-opacity duration-300 z-0\">
                            <svg class=\"absolute bottom-0 right-0 w-full h-full opacity-60 pointer-events-none\" viewBox=\"0 0 100 100\" preserveAspectRatio=\"none\">
                                <path d=\"M100,100 L100,40 C80,70 50,90 0,100 Z\" fill=\"rgba(64,158,255,0.06)\"></path>
                                <path d=\"M100,100 L100,0 C70,40 30,80 0,100 Z\" fill=\"rgba(64,158,255,0.04)\"></path>
                            </svg>
                        </div>
                        <div class=\"relative z-10 p-5 flex flex-col h-full\">
                            <div class=\"flex justify-between items-start mb-4\">
                                <div class=\"flex items-center gap-3\">
                                    <div class=\"w-11 h-11 rounded-full bg-[#1c7ffd] text-white flex items-center justify-center text-xl shadow-sm shrink-0\">
                                        <i class=\"fa-solid fa-envelope\"></i>
                                    </div>
                                    <div class=\"flex flex-col\">
                                        <span class=\"text-[#303133] font-bold text-[15px] truncate w-32\" title=\"测试离线任务...\">测试离线任务...</span>
                                        <span class=\"text-[#909399] text-[12px] mt-0.5\">任务ID：CJ20260521001</span>
                                    </div>
                                </div>
                                <div class=\"bg-[#1c7ffd] text-white px-2 py-0.5 rounded-full text-[11px] flex items-center shadow-sm whitespace-nowrap\">
                                    <i class=\"fa-solid fa-circle-check mr-1\"></i> 草稿
                                </div>
                            </div>
                            <div class=\"border-b border-gray-100 mb-3 group-hover:border-blue-100 transition-colors duration-300\"></div>
                            <div class=\"flex flex-col gap-1.5 mb-auto\">
                                <span class=\"text-[#606266] text-[13px] truncate\" title=\"任务描述：测试离线任务_20260521001\">任务描述：测试离线任务_20260521001</span>
                                <div class=\"flex items-center gap-6 text-[#909399] text-[13px] mt-1\">
                                    <span>数据资源数：1</span>
                                    <span>数据产品数：0</span>
                                    <span>公共数据产品数：0</span>
                                </div>
                            </div>
                            <div class=\"relative h-8 mt-4 overflow-hidden\">
                                <div class=\"absolute inset-0 flex items-center text-[#909399] text-[12px] transition-all duration-300 group-hover:opacity-0 group-hover:translate-y-4\">
                                    任务开始时间：2026-05-21 &nbsp;&nbsp; 任务截止时间：2026-12-31
                                </div>
                                <div class=\"absolute inset-0 flex items-center gap-2 opacity-0 translate-y-4 transition-all duration-300 group-hover:opacity-100 group-hover:translate-y-0\">
                                    <a href=\"scene_detail.html\" class=\"flex-1 text-center py-1.5 bg-white border border-gray-200 rounded text-[#606266] hover:text-[#1c7ffd] hover:border-[#1c7ffd] hover:bg-blue-50 text-[12px] transition-colors shadow-sm cursor-pointer\">任务详情</a>
                                    <button class=\"flex-1 text-center py-1.5 bg-white border border-gray-200 rounded text-[#606266] hover:text-[#1c7ffd] hover:border-[#1c7ffd] hover:bg-blue-50 text-[12px] transition-colors shadow-sm cursor-pointer\">数据资源</button>
                                    <a href=\"sql_develop.html?nav=sandbox-task\" class=\"flex-1 text-center py-1.5 bg-white border border-gray-200 rounded text-[#606266] hover:text-[#1c7ffd] hover:border-[#1c7ffd] hover:bg-blue-50 text-[12px] transition-colors shadow-sm cursor-pointer\">在线开发</a>
                                    <a href=\"dev_team.html\" class=\"flex-1 text-center py-1.5 bg-white border border-gray-200 rounded text-[#606266] hover:text-[#1c7ffd] hover:border-[#1c7ffd] hover:bg-blue-50 text-[12px] transition-colors shadow-sm cursor-pointer\">开发者</a>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Card 6 -->
                    <div class=\"group relative bg-white rounded-lg shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] border border-gray-100 overflow-hidden flex flex-col h-[210px] transition-all hover:shadow-lg hover:border-blue-200 cursor-default\">
                        <div class=\"absolute inset-0 bg-gradient-to-br from-[#ffffff] via-[#f0f6ff] to-[#e1edff] opacity-0 group-hover:opacity-100 transition-opacity duration-300 z-0\">
                            <svg class=\"absolute bottom-0 right-0 w-full h-full opacity-60 pointer-events-none\" viewBox=\"0 0 100 100\" preserveAspectRatio=\"none\">
                                <path d=\"M100,100 L100,40 C80,70 50,90 0,100 Z\" fill=\"rgba(64,158,255,0.06)\"></path>
                                <path d=\"M100,100 L100,0 C70,40 30,80 0,100 Z\" fill=\"rgba(64,158,255,0.04)\"></path>
                            </svg>
                        </div>
                        <div class=\"relative z-10 p-5 flex flex-col h-full\">
                            <div class=\"flex justify-between items-start mb-4\">
                                <div class=\"flex items-center gap-3\">
                                    <div class=\"w-11 h-11 rounded-full bg-[#1c7ffd] text-white flex items-center justify-center text-xl shadow-sm shrink-0\">
                                        <i class=\"fa-solid fa-envelope\"></i>
                                    </div>
                                    <div class=\"flex flex-col\">
                                        <span class=\"text-[#303133] font-bold text-[15px] truncate w-32\" title=\"隐私计算任务_222003\">隐私计算任务_...</span>
                                        <span class=\"text-[#909399] text-[12px] mt-0.5\">任务ID：CJ20262220003</span>
                                    </div>
                                </div>
                                <div class=\"bg-[#1c7ffd] text-white px-2 py-0.5 rounded-full text-[11px] flex items-center shadow-sm whitespace-nowrap\">
                                    <i class=\"fa-solid fa-circle-check mr-1\"></i> 开发中
                                </div>
                            </div>
                            <div class=\"border-b border-gray-100 mb-3 group-hover:border-blue-100 transition-colors duration-300\"></div>
                            <div class=\"flex flex-col gap-1.5 mb-auto\">
                                <span class=\"text-[#606266] text-[13px] truncate\" title=\"任务描述：山东亿云信息技术有限公司离线任务...\">任务描述：山东亿云信息技术有限公司离...</span>
                                <div class=\"flex items-center gap-6 text-[#909399] text-[13px] mt-1\">
                                    <span>数据资源数：1</span>
                                    <span>数据产品数：0</span>
                                    <span>公共数据产品数：0</span>
                                </div>
                            </div>
                            <div class=\"relative h-8 mt-4 overflow-hidden\">
                                <div class=\"absolute inset-0 flex items-center text-[#909399] text-[12px] transition-all duration-300 group-hover:opacity-0 group-hover:translate-y-4\">
                                    任务开始时间：2026-05-12 &nbsp;&nbsp; 任务截止时间：2026-12-31
                                </div>
                                <div class=\"absolute inset-0 flex items-center gap-2 opacity-0 translate-y-4 transition-all duration-300 group-hover:opacity-100 group-hover:translate-y-0\">
                                    <a href=\"scene_detail.html\" class=\"flex-1 text-center py-1.5 bg-white border border-gray-200 rounded text-[#606266] hover:text-[#1c7ffd] hover:border-[#1c7ffd] hover:bg-blue-50 text-[12px] transition-colors shadow-sm cursor-pointer\">任务详情</a>
                                    <button class=\"flex-1 text-center py-1.5 bg-white border border-gray-200 rounded text-[#606266] hover:text-[#1c7ffd] hover:border-[#1c7ffd] hover:bg-blue-50 text-[12px] transition-colors shadow-sm cursor-pointer\">数据资源</button>
                                    <a href=\"sql_develop.html?nav=sandbox-task\" class=\"flex-1 text-center py-1.5 bg-white border border-gray-200 rounded text-[#606266] hover:text-[#1c7ffd] hover:border-[#1c7ffd] hover:bg-blue-50 text-[12px] transition-colors shadow-sm cursor-pointer\">在线开发</a>
                                    <a href=\"dev_team.html\" class=\"flex-1 text-center py-1.5 bg-white border border-gray-200 rounded text-[#606266] hover:text-[#1c7ffd] hover:border-[#1c7ffd] hover:bg-blue-50 text-[12px] transition-colors shadow-sm cursor-pointer\">开发者</a>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </main>
    </div>

    <!-- 创建任务弹窗 -->
    <div id=\"createTaskOverlay\" class=\"fixed inset-0 bg-black/40 hidden z-40\" onclick=\"closeCreateTaskModal()\"></div>
    <div id=\"createTaskModal\" class=\"fixed top-1/2 left-1/2 w-[640px] max-w-[calc(100vw-32px)] bg-white rounded-xl shadow-2xl z-50 -translate-x-1/2 -translate-y-1/2 hidden\">
        <div class=\"h-14 flex items-center justify-between px-6 border-b border-gray-100\">
            <span class=\"text-[16px] font-bold text-[#303133]\">创建任务</span>
            <button onclick=\"closeCreateTaskModal()\" class=\"text-gray-400 hover:text-[#1c7ffd] transition-colors\">
                <i class=\"fa-solid fa-xmark text-lg\"></i>
            </button>
        </div>
        <div class=\"p-6 flex flex-col gap-5\">
            <div class=\"flex items-center\">
                <label class=\"w-[120px] shrink-0 text-right text-[#606266]\"><span class=\"text-red-500 mr-1\">*</span>任务名称：</label>
                <input id=\"taskNameInput\" type=\"text\" placeholder=\"请输入任务名称\" class=\"ml-4 flex-1 border border-gray-300 rounded px-3 py-2 text-sm focus:outline-none focus:border-[#1c7ffd]\">
            </div>
            <div class=\"flex items-start\">
                <label class=\"w-[120px] shrink-0 text-right text-[#606266] mt-2\"><span class=\"text-red-500 mr-1\">*</span>已申请的数据资源：</label>
                <div class=\"ml-4 flex-1 grid grid-cols-2 gap-3\">
                    <label class=\"flex items-center gap-2 border border-gray-200 rounded-lg px-3 py-2 hover:border-[#1c7ffd] cursor-pointer\">
                        <input type=\"checkbox\" class=\"w-4 h-4 text-[#1c7ffd] focus:ring-[#1c7ffd]\">
                        <span>企业基础信息库</span>
                    </label>
                    <label class=\"flex items-center gap-2 border border-gray-200 rounded-lg px-3 py-2 hover:border-[#1c7ffd] cursor-pointer\">
                        <input type=\"checkbox\" class=\"w-4 h-4 text-[#1c7ffd] focus:ring-[#1c7ffd]\">
                        <span>经营变更记录表</span>
                    </label>
                    <label class=\"flex items-center gap-2 border border-gray-200 rounded-lg px-3 py-2 hover:border-[#1c7ffd] cursor-pointer\">
                        <input type=\"checkbox\" class=\"w-4 h-4 text-[#1c7ffd] focus:ring-[#1c7ffd]\">
                        <span>企业标签接口</span>
                    </label>
                    <label class=\"flex items-center gap-2 border border-gray-200 rounded-lg px-3 py-2 hover:border-[#1c7ffd] cursor-pointer\">
                        <input type=\"checkbox\" class=\"w-4 h-4 text-[#1c7ffd] focus:ring-[#1c7ffd]\">
                        <span>税务风险评估接口</span>
                    </label>
                </div>
            </div>
            <div class=\"flex items-start\">
                <label class=\"w-[120px] shrink-0 text-right text-[#606266] mt-2\"><span class=\"text-red-500 mr-1\">*</span>开发者账号：</label>
                <div class=\"ml-4 flex-1 grid grid-cols-2 gap-3\">
                    <label class=\"flex items-center gap-2 border border-gray-200 rounded-lg px-3 py-2 hover:border-[#1c7ffd] cursor-pointer\">
                        <input type=\"checkbox\" class=\"w-4 h-4 text-[#1c7ffd] focus:ring-[#1c7ffd]\">
                        <span>yiyun</span>
                    </label>
                    <label class=\"flex items-center gap-2 border border-gray-200 rounded-lg px-3 py-2 hover:border-[#1c7ffd] cursor-pointer\">
                        <input type=\"checkbox\" class=\"w-4 h-4 text-[#1c7ffd] focus:ring-[#1c7ffd]\">
                        <span>wangyu</span>
                    </label>
                    <label class=\"flex items-center gap-2 border border-gray-200 rounded-lg px-3 py-2 hover:border-[#1c7ffd] cursor-pointer\">
                        <input type=\"checkbox\" class=\"w-4 h-4 text-[#1c7ffd] focus:ring-[#1c7ffd]\">
                        <span>liuliu</span>
                    </label>
                </div>
            </div>
        </div>
        <div class=\"px-6 py-4 border-t border-gray-100 flex justify-end gap-3\">
            <button onclick=\"closeCreateTaskModal()\" class=\"px-6 py-1.5 border border-gray-300 rounded text-[#606266] hover:text-[#1c7ffd] hover:border-[#1c7ffd] transition-colors text-sm bg-white\">取消</button>
            <button onclick=\"createTask()\" class=\"px-6 py-1.5 bg-[#1c7ffd] text-white rounded hover:bg-blue-500 transition-colors text-sm\">创建任务</button>
        </div>
    </div>

    <div id=\"toast\" class=\"fixed top-6 left-1/2 -translate-x-1/2 bg-[#f0f9eb] border border-[#e1f3d8] text-[#67c23a] px-4 py-2 rounded shadow-sm z-50 flex items-center gap-2 transition-all duration-300 opacity-0 -translate-y-4 pointer-events-none\">
        <i class=\"fa-solid fa-circle-check\"></i>
        <span>任务创建成功</span>
    </div>

    <script>
        function openCreateTaskModal() {
            document.getElementById('createTaskOverlay').classList.remove('hidden');
            document.getElementById('createTaskModal').classList.remove('hidden');
        }

        function closeCreateTaskModal() {
            document.getElementById('createTaskOverlay').classList.add('hidden');
            document.getElementById('createTaskModal').classList.add('hidden');
        }

        function createTask() {
            const toast = document.getElementById('toast');
            closeCreateTaskModal();
            toast.classList.remove('opacity-0', '-translate-y-4');
            toast.classList.add('opacity-100', 'translate-y-0');
            setTimeout(() => {
                toast.classList.add('opacity-0', '-translate-y-4');
                toast.classList.remove('opacity-100', 'translate-y-0');
            }, 1500);
        }
    </script>
</body>
</html>""")
