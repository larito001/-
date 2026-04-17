# 洛克王国：世界 - 自动战斗工具

针对《洛克王国：世界》的自动战斗辅助工具，通过屏幕截图 + 模板匹配识别游戏界面状态，自动完成战斗操作。

> **声明：** 非商业售卖，仅供学习娱乐。最终解释权归开发者 Larito 所有。

## 功能

通过 OpenCV 模板匹配识别当前游戏界面，自动执行对应操作：

| 界面状态 | 识别方式 | 自动操作 |
|---------|---------|---------|
| 回能状态（buttonPage） | 左下角匹配星形按钮模板 | 点击星形按钮（使用默认技能） |
| 选择状态（selectHero） | 右侧战报图标 + 右下角逃跑按钮（Canny 边缘匹配） | 依次按 1~6 + 空格，逐个尝试出战精灵 |
| 等待状态（normal） | 无匹配 | 等待，偶尔随机移动鼠标 |

### 特性

- **Nuitka 原生编译** — 编译为 C 代码，无 Python 运行时解包特征（区别于 PyInstaller）
- **PostMessage 输入** — 通过窗口消息队列发送输入，绕过 SendInput 的 INJECTED 标记
- **Canny 边缘匹配** — select 状态使用边缘检测匹配，不受背景颜色/高亮影响
- **连续确认机制** — select 状态需连续检测 2 次才执行，消除偶发误判
- **人性化模拟** — 贝塞尔曲线鼠标轨迹 + 随机抖动 + 会话节奏 + 疲劳曲线 + 微失误
- **GUI 控制面板** — 深色主题界面，实时显示检测状态（回能/选择/等待）
- **全局热键** — GetAsyncKeyState 随机间隔轮询，无系统钩子注册
- **自动提权** — 启动时自动请求管理员权限

### 反检测架构

| 检测向量 | 防御措施 |
|---------|---------|
| 输入注入标志（LLMHF_INJECTED） | PostMessage + SetCursorPos，不经过 SendInput |
| PyInstaller 特征 | Nuitka + MSVC 编译为原生 C，无 python3x.dll / _MEIPASS |
| 进程名/签名扫描 | 随机系统进程名 + 匹配 Windows 版本信息资源 |
| DXGI 接口监控 | DXGI 为主截屏，GDI 自动回退 |
| API 调用频率特征 | GetAsyncKeyState 随机间隔轮询（10-35ms） |
| 服务端 AI 行为分析 | 会话节奏 + 疲劳曲线 + 随机分心 + 定时休息 + 微失误 |
| 窗口标题枚举 | 每次启动随机生成无特征标题 |
| 内存字符串扫描 | 已清除敏感关键词 |

## 快捷键

| 按键 | 功能 |
|------|------|
| F6 | 暂停 / 恢复 |
| F7 | 重新框选游戏区域 |
| Esc | 退出程序 |

## 使用方法

### 环境要求

- Windows 10/11
- Python 3.8+
- Visual Studio 2022 Build Tools（Nuitka 编译需要 MSVC）
- 游戏分辨率设置为 **1176 x 664**

### 依赖安装

启动时会自动检测依赖，缺少任何一项都会弹窗提示并阻止启动。

```bash
pip install opencv-python numpy dxcam
```

编译依赖（打包时自动安装）：

```bash
pip install nuitka ordered-set zstandard
```

### 直接运行

```bash
python src/auto_battle.py
```

### 打包为 EXE

双击 `build.bat` 或运行：

```bash
python build.py
```

打包后的 EXE 位于 `Build/` 目录下，文件名为随机生成的类系统进程名（如 `svchost_abcd.exe`），可独立运行。

首次编译较慢（Nuitka 需要将 Python 编译为 C），后续编译有缓存会快很多。

## 操作步骤

1. 运行工具（会自动弹出 UAC 管理员权限请求）
2. 在控制面板点击「选择区域」或按 F7，拖拽框选游戏窗口
3. 点击「开始」，工具自动初始化后端并开始运行
4. 控制面板实时显示当前检测状态（回能/选择/等待）
5. 按 F6 随时暂停/恢复，按 Esc 退出

## 项目结构

```
├── src/
│   ├── auto_battle.py      # 主程序（界面识别 + 自动操作 + 反检测）
│   ├── Button.jpg           # 模板 - 星形按钮（回能状态检测）
│   ├── BattleReport.png     # 模板 - 战报图标（选择状态检测）
│   ├── SelectRun.jpg        # 模板 - 逃跑按钮（选择状态检测）
│   └── .log/                # 运行日志
├── Build/                   # 编译输出目录（EXE 文件名随机）
├── build.py                 # Nuitka 编译脚本（自动随机化 EXE 名称 + 版本信息）
├── build.bat                # 一键打包批处理
└── .gitignore
```

## 联系方式

QQ: 275899142
