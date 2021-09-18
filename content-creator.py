#!/usr/bin/env python3



BOLD_TEXT_FONT = 30
NORMAL_TEXT_SIZE = 25
BKZ_TO_NAME = 6 # number of characters between the ( of a bkz and the first letter of the content it directs to
BACKGROUND_COLOR = "0xff800000"
TITLE2_COLOR = "lightBlue"
TITLE2_SIZE = NORMAL_TEXT_SIZE
NORMAL_INSTRUCTION_PREFIX = "•" + " " 
SUB_INSTRUCTION_PREFIX = "-" + " "
STRINGS_BASE_NAME = "metin"




def save_file(file_path : str, content : str):

    open(path + self.screen_file, "w").write(result)
    
def is_escape(string : str, index : int):
    i = 0
    index -= 1

    while (string[index] == '\\'):
        index -= 1
        i+= 1

    return i % 2


def find_bkz_end(instrcution, index):
    
    for i in xrange(index, len(instruction)):
        if instruction[i] == ")" and not is_escape(instruction, i):
            return index + i + 1

def add_indentation(string : str, indentation : str):
    
    array = string.split("\n")    
    
    for i in xrange(len(array)):
       array[i] = indentation + array[i]

    return "\n".join(array)


def generate_bkz(instruction, index):
    
    bkz_end = find_bkz_end(instruction, index)
    bkz_text = instruction[index - BKZ_TO_NAME : bkz_end + 1]
    content_name = instruction[index : bkz_end]

    result = f"""\n

    \n""" burayı yappppp

def generate_string(instruction : str, number : int):

    return f"String {STRINGS_BASE_NAME}{str(number)} = \"{instruction}\";"

def generate_instruction(bkzlar : tuple, number : int):

   result = f"""\n
Row(
  children: [
    Expanded(
      child: Text(
        {STRINGS_BASE_NAME}{str(number)},
        style: TextStyle(fontsize: 25),
      ),
    ),
  ],
),
        """

    for i in range(len(bkzlar)):

        bkz ="""\n
Row(
    children: [
      Container(
        margin: EdgeInsets.fromLTRB(5,5,5,5),
        child: InkWell(
          child: Text(bkz{number},
            style: TextStyle(fontFamily: "Times", fontSize: 25, color: Colors.lightBlue),
          ),
          onTap: () {
        Navigator.push(context,
            MaterialPageRoute(builder: (context) => {input(f\"Name for the content {bkzlar[i][BKZ_TO_NAME + 1 : find_bkz_end(bkzlar[i])]} as bkz: \")}()));
      },
        ),
      )
    ],
  ),
            """

        result += f"\n{bkz}"


    return result


def generate_link(link : str):
    
    result = f"""
Row(
  children: [
    Expanded(
        child:  Image.network('{link}')
    ),
  ],
),
Text(" "),
"""
    return result



def generate_screen_code(file_name, title1, title2, header_image):


        result = f"""
import 'package:flutter/material.dart';
import 'dart:ui';
import 'package:fiyboz_rehber/ingredients/{file_name}/{test_file}';
import 'package:fiyboz_rehber/ingredients/{file_name}/{ss_file}';

class {file_name.title()} extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Color(BACKGROUND_COLOR),
        title: Text('{title1}'),
      ),
      body: ListView(
        children: [
          Container(
            child: Image(
              image: AssetImage('images/'{header_image}'),
            ),
          ),
          Container(
            margin: EdgeInsets.fromLTRB(15, 15, 15, 15),
            child: Row(
              children: [
                Expanded(
                  child: Text(
                    '{title2}',
                    style: TextStyle(fontsizze: {str(TITLE2_SIZE)}, color: Colors.{TITLE2_COLOR}),
                  ),
                ),
              ],
            ),
          ),
          {file_name.title()}Text(),
          {file_name.title()}Ss(),
        ],
      ),
    );
  }
}
        """

    return result


def generate_instruction_code(instructions : Instruction, file_name : str):

    result = f"""
import 'package:flutter/material.dart';
import 'dart:ui;

class {{file_name.title().title()}text extends StatelessWidget{
  @override
  Widget build(BuildContext context) {
    """

    indentation = "    "

    for i in xrange(len(instructions)):

        result += f"\n{add_indentation(generate_string(instructions[i].instruction, i), indentation)}"


    result += """\n
    return Container(
      margin: EdgeInsets.fromTRB(12, 12, 12, 12),
      child: Column(
        children: [
        """


    indentation = "          "

    for i in xrange(len(instructions)):

        result += f"\n{add_indentation(generate_instruction(instructions[i].bkzlar, i), indentation)}"
        
        
        result += """\n
        ],
      ),
    );
  }
}\n
        """
    return result
        

def genrrate_ss_code(links : str, file_name : str):

        result = f"""
import 'package:flutter/material.dart';
import 'dart:ui';

class {file_name.title()}Ss extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
        margin: EdgeInsets.fromLTRB(15, 15, 15, 15),
        child: Column(
          children: [
              
        """

        indentation = "            "

        for link in links:
            result += f"\n{add_indentation(generate_link(link), indentation}"

        result += """\n
              ],
            ),
          ],
        ));
  }
}
            """
        return result



class Instruction:

    number = 0

    @create // generating instruction no Instruction.number, generated instrcution Instruction.number
    def __init__(self, instruction : str, is_sub : bool, actions : tuple):

        if is_sub:
            instruction = SUB_INSTRUCTION_PREFIX + instruction
        else:
            instruction = NORMAL_INSTRUCTION_PREFIX + instruction
            
        self.instruction = ""
        self.bkzlar = []
        bkz_count = 0
        i = 0
        while i < len(instruction):
            if in_action:
                in_action -= 1
                self.instruction += instruction[i].lowercase()

                if not in_action:
                    self.instruction += "\""
            
            
            if instruction[i : i + BKZ_TO_NAME] == "(bkz." and not is_escape(instruction, i):

                bkz_count += 1
               
                bkz_end = find_bkz_end(instruction, i + BKZ_TO_NAME)
                self.instruction += f"(bkz. Yönergedeki {bkz_count}. bkz)"
                i = bkz_end
                self.bkzlar.append(instruction[i + BKZ_TO_NAME : bkz_end]) 

                continue

            

            for j in xrange(len(actions)):
                if instruction[i : i + len(action_path[j])] == action_path[j]:
                    self.instruction += f"'{instruction[i : i + len(action_path[j])].title()}'"
                    i += len(action_path[j]) - 1
                    continue 
                        
            self.instruction += instruction[i]
        
            i += 1
            
        self.bkzlar = tuple(self.bkzlar)

        Instruction.number += 1
        


class Content:

    def __init__(self, file_name : str, header_image : str, titles : tuple, action_path : tuple, instructions : tuple, links : tuple):

        self.file_name = file_name
        self.screen_file = f"{self.file_name}.dart"
        self.text_file = f"{self.file_name}text.dart"
        self.ss_file = f"{self.file_name}ss.dart"

        self.header_image = header_image # first image in the content page
        self.title1 = titles[0] # title at the very top
        self.title2 = titles[1] # title under the header image
        self.action_path = action_path
        self.instructions = instructions ## the list consists of items from Instruction class
        self.links = links

        self.path = "~/Desktop/"

    def create_screen(self, path : str):

        print("Creating screen file!")  

        result = generate_screen_code(self.file_name, self.title1, self.title2, self.header_image)
        save_file(self.path + self.screen_file, result)


        print(f"Screen file is saved to {path}{self.screen_file}!")

    def create_text(self, path : str):

        print("creating instructions!")

        result = generate_instruction_code(self.instructions, self.file_name)

        save_file(self.path + self.ss_file, result)

    def create_sss(self, path : str):

        print("creating ss!")

        result = generate_ss_code(self.links, self.file_name)

        save_file(self.path + self.ss_file, result)


    def create_files(self, path : str):

        print("Creating files!")

        self.create_screen(path)
        self.create_text(path)
        self.create_sss(path)

        print("Created files in Desktop!")
        



def get_file_name():
    return input("template file name (e.g. hotspot): ")

def get_header_image():
    return input("header image name (with extension): ")

def get_titles():
    return (input("Title 1: "), input("Title 2: "))

def get_action_path():
    result = [] 
    while (result[-1] != "."):
        result.append(input("next action destination (. means quit): "))

    return tuple(result[: -1])

def get_instructions(action_path : tuple):
    result = [] 
    while (result[-1] != "."):
        result.append(Instruction(input("next instruction (. means quit): "), True if input("instruction type (1 : sub, 2 : normal):)" else False,  action_path))

    return tuple(result[: -1])

def get_links():
    result = [] 
    while (result[-1] != "."):
        result.append(input("next image link (. means quit): "))

    return tuple(result[: -1])


def get_inputs():

    action_path = get_action_path()
    content = Content(get_file_name(), get_header_image(), get_titles(), action_path, get_instructions(action_path), get_links())
    
    return content



def main():

    content = get_inputs()
    content.create_files(input("path to save files to (add / or \ at the end!): ")

if __name__ == "__main__":
    main()
        
