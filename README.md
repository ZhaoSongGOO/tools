# Tools

---

## How To USE

```(shell)
git clone git@gitee.com:zhaosong-lmm_admin/tools.git
source tools/envsetup.sh
```

---

## Tools List

### 1. check-format

#### 1.1 功能介绍

用于代码风格格式化，目前使用的code-style为[google code style](https://google.github.io/styleguide/)，具体支持的参数如下：

```(shell)
optional arguments:
  -h, --help            show this help message and exit
  -mode MODE, -m MODE   0 [default]: Check all files 
                        1 :Check change files in current commit
  -path PATH, -p PATH   The path where the formatted code file is located. 
                        The default path is the current one
  -verbose VERBOSE, -v VERBOSE
                        Whether to visualize the inspection process,on or off[default]
  -language LANGUAGE, -l LANGUAGE
                        file Type all[default] c[c language and cpp] j[java] o[object c]
```

