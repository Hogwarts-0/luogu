import os
import subprocess
import customtkinter as ctk
from tkinter import filedialog, messagebox

# 初始化 UI 主题
ctk.set_appearance_mode("dark")  # 主题: "dark" or "light"
ctk.set_default_color_theme("blue")  # 颜色主题


class TestcaseGenerator(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("📂 测试点生成工具")
        self.geometry("700x550")
        self.configure(bg="#1E1E1E")  # 设置背景颜色

        # 标题
        self.label_title = ctk.CTkLabel(self, text="🚀 测试点生成工具", font=("Arial", 24, "bold"), text_color="white")
        self.label_title.pack(pady=15)

        # 代码文件选择
        self.frame_code = ctk.CTkFrame(self, fg_color="#2E2E2E", corner_radius=10)
        self.frame_code.pack(pady=10, padx=20, fill="x")

        self.label_code = ctk.CTkLabel(self.frame_code, text="代码文件:", text_color="white")
        self.label_code.pack(side="left", padx=10)

        self.entry_code_path = ctk.CTkEntry(self.frame_code, width=400)
        self.entry_code_path.pack(side="left", padx=10)

        self.btn_select_code = ctk.CTkButton(self.frame_code, text="📂 选择", command=self.select_code_file)
        self.btn_select_code.pack(side="left", padx=10)

        # 输入框
        self.label_input = ctk.CTkLabel(self, text="输入测试数据（每组用空行分隔）:", text_color="white")
        self.label_input.pack(pady=5)

        self.text_input = ctk.CTkTextbox(self, width=600, height=150)
        self.text_input.pack(pady=5)

        # 选择保存路径
        self.frame_save = ctk.CTkFrame(self, fg_color="#2E2E2E", corner_radius=10)
        self.frame_save.pack(pady=10, padx=20, fill="x")

        self.label_save = ctk.CTkLabel(self.frame_save, text="保存路径:", text_color="white")
        self.label_save.pack(side="left", padx=10)

        self.entry_save_path = ctk.CTkEntry(self.frame_save, width=400)
        self.entry_save_path.pack(side="left", padx=10)

        self.btn_select_save = ctk.CTkButton(self.frame_save, text="📂 选择", command=self.select_save_path)
        self.btn_select_save.pack(side="left", padx=10)

        # 生成按钮
        self.btn_generate = ctk.CTkButton(self, text="🚀 生成测试点", command=self.generate_test_files, fg_color="green")
        self.btn_generate.pack(pady=20)

        # 进度条
        self.progress = ctk.CTkProgressBar(self, width=500)
        self.progress.pack(pady=10)
        self.progress.set(0)

    def select_code_file(self):
        """ 选择代码文件 """
        file_path = filedialog.askopenfilename(filetypes=[("Python 文件", "*.py"), ("C++ 文件", "*.cpp")])
        if file_path:
            self.entry_code_path.delete(0, "end")
            self.entry_code_path.insert(0, file_path)

    def select_save_path(self):
        """ 选择测试点保存路径 """
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.entry_save_path.delete(0, "end")
            self.entry_save_path.insert(0, folder_path)

    def run_program(self, program_path, input_data):
        """ 运行代码文件 """
        try:
            if program_path.endswith('.py'):
                cmd = ['python', program_path]
            elif program_path.endswith('.cpp'):
                exe_file = program_path.replace('.cpp', '.exe')
                if not os.path.exists(exe_file):
                    subprocess.run(['g++', program_path, '-o', exe_file], check=True)
                cmd = [exe_file]
            else:
                return "Error: 仅支持 Python 和 C++"

            result = subprocess.run(cmd, input=input_data, text=True, capture_output=True, timeout=5)
            return result.stdout.strip()

        except subprocess.TimeoutExpired:
            return "Error: 运行超时"
        except subprocess.CalledProcessError as e:
            return f"Error: 运行失败 {e}"
        except Exception as e:
            return f"Error: {e}"

    def generate_test_files(self):
        """ 生成测试点 """
        program_path = self.entry_code_path.get()
        save_path = self.entry_save_path.get()
        raw_input_data = self.text_input.get("1.0", "end").strip()

        if not program_path:
            messagebox.showerror("错误", "请选择代码文件！")
            return
        if not save_path:
            messagebox.showerror("错误", "请选择保存路径！")
            return
        if not raw_input_data:
            messagebox.showerror("错误", "请输入测试数据！")
            return

        # **数据格式优化**
        test_cases = [case.strip() for case in raw_input_data.split("\n\n") if case.strip()]  # 按 **空行** 分割，去除空格

        if not test_cases:
            messagebox.showerror("错误", "输入数据格式不正确！请检查换行符。")
            return

        os.makedirs(save_path, exist_ok=True)
        total_tests = len(test_cases)

        for i, input_data in enumerate(test_cases, start=1):
            index = f"{i:03d}"
            input_file = os.path.join(save_path, f"{index}.in")
            output_file = os.path.join(save_path, f"{index}.out")

            # **格式化 & 规范数据**
            input_data_cleaned = "\n".join(line.strip() for line in input_data.split("\n") if line.strip())

            with open(input_file, "w", encoding="utf-8") as f:
                f.write(input_data_cleaned + "\n")  # 确保正确换行

            output_data = self.run_program(program_path, input_data_cleaned)

            with open(output_file, "w", encoding="utf-8") as f:
                f.write(output_data.rstrip("\n") + "\n")  # 确保最后一行有换行

            self.progress.set(i / total_tests)  # 更新进度条

        messagebox.showinfo("完成", f"测试点已生成！保存在：{save_path}")


if __name__ == "__main__":
    app = TestcaseGenerator()
    app.mainloop()