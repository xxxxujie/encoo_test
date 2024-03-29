import pathlib


class Config:
    # 获取当前的文件路径
    current_path = pathlib.Path(__file__).absolute()
    # 获取项目的根目录
    root_dir = current_path.parent.parent
    # 测试数据存储目录
    data_dir = root_dir / 'data'
    # cases 文件
    case_file = data_dir / 'cases.xlsx'

    front_host = ''

    admin_host = ''


if __name__ == '__main__':
    print(Config.current_path)