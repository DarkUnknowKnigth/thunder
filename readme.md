# Thunder
## (CLI) flask mvc comand line 
Thunder has been created to made easier develop mvc applications with the microframework Flask

| key | Control | |
| ------ | ------ |----|
| thunder | init / exit||
|  |  **_generate_**| |
||new|name / _path_|
|  | **_directive_** |
|  | add | name|
|  | make | name|
|  | delete | name|
||  | **_component_** |
||  | route |
||  | model | name|
||  | View| name|
||  | controller | name
|| **_Parameters_**| 
||- -help|
||- -browser|
||- -version|


### Examples
start project:
```sh
$ thunder new project
or
$ t new project
```
components:
You can create diferent components like models, views, cotrollers or routes just typing the following commands:
#### add 
Add code to your project
```sh
$ t add route [name]
```
#### make
Make code with commands
```sh
$ t make model [name]
```
#### delete
Delete componets to your project
```sh
$ t delete controler [name]
```
### Helpers

```sh
$ t --help 

$ t --browser

$ t --version
```
License
----

put a license here