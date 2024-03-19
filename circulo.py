"""Animation example"""
import OpenGL.GL as GL

from core.base import Base
from core.utils import Utils
from core.attribute import Attribute
from core.uniform import Uniform
import math


class Example(Base):
    def initialize(self):
        print("Initializing program...")
        # Initialize program #
        vs_code = """
            in vec3 position;
            uniform vec3 translation;
            void main()
            {
                vec3 pos = position + translation;
                gl_Position = vec4(pos.x+0.5, pos.y, pos.z, 1.0);
            }
        """
        fs_code = """
            uniform vec3 baseColor;
            out vec4 fragColor;
            void main()
            {
                fragColor = vec4(baseColor.r, baseColor.g, baseColor.b, 1.0);
            }
        """
        self.program_ref = Utils.initialize_program(vs_code, fs_code)

        # render settings (optional) #
        # Specify color used when clearly
        GL.glClearColor(0.0, 0.0, 0.0, 1.0)
        # Set up vertex array object #
        
        self.vao_K_first = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_K_first)
        position_K_first  = [[-0.64,  0.51,  0.0],
                             [-0.79,  0.46,  0.0],
                             [-0.63,  0.46,  0.0],
                             [-0.63,  0.5,  0.0],
                        
                        ]
        self.vertex_count_K_first = len(position_K_first)
        position_attribute_K_first = Attribute('vec3', position_K_first)
        position_attribute_K_first.associate_variable(self.program_ref, 'position')


        self.vao_K_second = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_K_second )
        position_K_second   = [ [-0.63,  0.46,  0.0],
                                [-0.79,  0.46,  0.0],
                                [-0.78,  0.13,  0.0],
                                [-0.64,  0.13,  0.0]]
        self.vertex_count_K_second  = len(position_K_second )
        position_attribute_K_second  = Attribute('vec3', position_K_second )
        position_attribute_K_second .associate_variable(self.program_ref, 'position') 

        
        self.vao_K_third = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_K_third )
        position_K_third   = [[-0.78,  0.13,  0.0],
                              [-0.78, -0.12,  0.0],
                              [-0.65, -0.12,  0.0],
                              [-0.64,  0.13,  0.0]]
        self.vertex_count_K_third  = len(position_K_third )
        position_attribute_K_third  = Attribute('vec3', position_K_third )
        position_attribute_K_third .associate_variable(self.program_ref, 'position') 


        self.vao_K_fourth = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_K_fourth )
        position_K_fourth   = [[-0.65,  -0.12,  0.0],
                                [-0.78,  -0.12,  0.0],
                                [-0.78,  -0.37,  0.0],
                                [-0.76,  -0.38,  0.0],
                                [-0.64,  -0.33,  0.0],]
        self.vertex_count_K_fourth  = len(position_K_fourth )
        position_attribute_K_fourth  = Attribute('vec3', position_K_fourth )
        position_attribute_K_fourth .associate_variable(self.program_ref, 'position') 



        self.vao_K_fifth = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_K_fifth )
        position_K_fifth   = [[-0.65,  0.13,  0.0],
                              [-0.62,  0.12,  0.0],
                              [-0.63,  0.04,  0.0],
                              [-0.65,  0.03,  0.0],]
        self.vertex_count_K_fifth  = len(position_K_fifth )
        position_attribute_K_fifth  = Attribute('vec3', position_K_fifth )
        position_attribute_K_fifth .associate_variable(self.program_ref, 'position') 

        self.vao_K_sixth = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_K_sixth )
        position_K_sixth   = [[-0.57,  0.19,  0.0],
                              [-0.63,  0.12,  0.0],
                              [-0.63,  0.04,  0.0],
                              [-0.61,  0.02,  0.0],
                              [-0.52,  0.14,  0.0],]
        self.vertex_count_K_sixth = len(position_K_sixth )
        position_attribute_K_sixth  = Attribute('vec3', position_K_sixth )
        position_attribute_K_sixth .associate_variable(self.program_ref, 'position') 


        self.vao_K_seventh = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_K_seventh )
        position_K_seventh   = [[-0.47,  0.28,  0.0],
                              [-0.57,  0.19,  0.0],
                              [-0.52,  0.14,  0.0],
                              [-0.47,  0.19,  0.0],
                              [-0.43,  0.22,  0.0],]
        self.vertex_count_K_seventh = len(position_K_seventh )
        position_attribute_K_seventh  = Attribute('vec3', position_K_seventh )
        position_attribute_K_seventh .associate_variable(self.program_ref, 'position') 


        self.vao_K_eighth = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_K_eighth )
        position_K_eighth   = [[-0.47,  0.28,  0.0],
                                [-0.43,  0.22,  0.0],
                              [-0.33,  0.29,  0.0],
                              [-0.37,  0.36,  0.0],]
        self.vertex_count_K_eighth = len(position_K_eighth )
        position_attribute_K_eighth  = Attribute('vec3', position_K_eighth )
        position_attribute_K_eighth .associate_variable(self.program_ref, 'position') 

        self.vao_K_ninth = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_K_ninth )
        position_K_ninth   = [[-0.23,  0.35,  0.0],
                              [-0.28,  0.43,  0.0],
                              [-0.37,  0.36,  0.0],
                              [-0.33,  0.29,  0.0],]
        self.vertex_count_K_ninth = len(position_K_ninth )
        position_attribute_K_ninth  = Attribute('vec3', position_K_ninth )
        position_attribute_K_ninth .associate_variable(self.program_ref, 'position') 


        self.vao_K_tenth = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_K_tenth )
        position_K_tenth   = [[-0.1,  0.41,  0.0],
                                [-0.19,  0.49,  0.0],
                              [-0.28,  0.43,  0.0],
                              [-0.23,  0.35,  0.0],]
        self.vertex_count_K_tenth = len(position_K_tenth )
        position_attribute_K_tenth  = Attribute('vec3', position_K_tenth  )
        position_attribute_K_tenth.associate_variable(self.program_ref, 'position') 

        self.vao_K_eleventh = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_K_eleventh )
        position_K_eleventh   = [[-0.05,  0.46,  0.0],
                                [-0.14,  0.52,  0.0],
                                [-0.19,  0.49,  0.0],
                                [-0.1,  0.41,  0.0],
                                [-0.05,  0.44,  0.0]]
        self.vertex_count_K_eleventh = len(position_K_eleventh )
        position_attribute_K_eleventh  = Attribute('vec3', position_K_eleventh  )
        position_attribute_K_eleventh.associate_variable(self.program_ref, 'position') 

        self.vao_K_twelfth = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_K_twelfth )
        position_K_twelfth   = [[-0.52  ,  0.14,  0.0],
                                [-0.61,  0.02,  0.0],
                                [-0.53,  -0.05,  0.0],]
        self.vertex_count_K_twelfth = len(position_K_twelfth )
        position_attribute_K_twelfth  = Attribute('vec3', position_K_twelfth  )
        position_attribute_K_twelfth.associate_variable(self.program_ref, 'position') 


        self.vao_K_thirteenth = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_K_thirteenth )
        position_K_thirteenth   = [[-0.41,  0.02,  0.0],
                                [-0.47,  0.07,  0.0],
                                [-0.53,  0.11,  0.0],
                                [-0.53,  -0.05,  0.0],
                                [-0.44,  -0.13,  0.0]]
        self.vertex_count_K_thirteenth = len(position_K_thirteenth )
        position_attribute_K_thirteenth  = Attribute('vec3', position_K_thirteenth  )
        position_attribute_K_thirteenth.associate_variable(self.program_ref, 'position')

        self.vao_K_fourteenth = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_K_fourteenth )
        position_K_fourteenth   = [[-0.41,  0.02,  0.0],
                                   [-0.44, -0.13,  0.0],
                                   [-0.37, -0.2,  0.0],
                                   [-0.28, -0.27,  0.0],
                                   [-0.24, -0.12,  0.0],
                                   [-0.33, -0.04,  0.0],]
        self.vertex_count_K_fourteenth = len(position_K_fourteenth )
        position_attribute_K_fourteenth  = Attribute('vec3', position_K_fourteenth  )
        position_attribute_K_fourteenth.associate_variable(self.program_ref, 'position')

        self.vao_K_fifteenth = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_K_fifteenth )
        position_K_fifteenth   = [[-0.12,  -0.21,  0.0],
                                   [-0.24, -0.12,  0.0],
                                   [-0.28, -0.27,  0.0],
                                   [-0.19, -0.34,  0.0],]
        self.vertex_count_K_fifteenth = len(position_K_fifteenth )
        position_attribute_K_fifteenth  = Attribute('vec3', position_K_fifteenth  )
        position_attribute_K_fifteenth.associate_variable(self.program_ref, 'position')
        

        self.vao_K_sixteenth = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_K_sixteenth )
        position_K_sixteenth   = [[-0.03,  -0.31,  0.0],
                                   [-0.03, -0.28,  0.0],
                                   [-0.12, -0.21,  0.0],
                                   [-0.19, -0.34,  0.0],
                                   [-0.15, -0.38,  0.0],]
        self.vertex_count_K_sixteenth = len(position_K_sixteenth )
        position_attribute_K_sixteenth  = Attribute('vec3', position_K_sixteenth  )
        position_attribute_K_sixteenth.associate_variable(self.program_ref, 'position')
        # Set up uniforms #
        self.translation = Uniform('vec3', [0.0, 0.0, 0.0])
        self.translation.locate_variable(self.program_ref, 'translation')
        self.base_color = Uniform('vec3', [0.0, 1.0, 0.0])
        self.base_color.locate_variable(self.program_ref, 'baseColor')

        self.timer = 0

    def update(self):
        """ Update data """

        self.timer += 0.01 
        self.translation.data[0] = math.sin(self.timer) * 0.5 ; 
        self.translation.data[1] = math.cos(self.timer) * 0.5  ; 

        

        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        GL.glUseProgram(self.program_ref)

        self.translation.upload_data()
        self.base_color.upload_data()
        GL.glBindVertexArray(self.vao_K_first)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_K_first)
        GL.glBindVertexArray(self.vao_K_second)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_K_second)
        GL.glBindVertexArray(self.vao_K_third)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_K_third)
        GL.glBindVertexArray(self.vao_K_fourth)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_K_fourth)
        GL.glBindVertexArray(self.vao_K_fifth)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_K_fifth)
        GL.glBindVertexArray(self.vao_K_sixth)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_K_sixth)
        GL.glBindVertexArray(self.vao_K_seventh)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_K_seventh)
        GL.glBindVertexArray(self.vao_K_eighth)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_K_eighth)
        GL.glBindVertexArray(self.vao_K_ninth)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_K_ninth)
        GL.glBindVertexArray(self.vao_K_tenth)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_K_tenth)
        GL.glBindVertexArray(self.vao_K_eleventh)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_K_eleventh)
        GL.glBindVertexArray(self.vao_K_twelfth)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_K_twelfth)
        GL.glBindVertexArray(self.vao_K_thirteenth)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_K_thirteenth)
        GL.glBindVertexArray(self.vao_K_fourteenth)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_K_fourteenth)
        GL.glBindVertexArray(self.vao_K_fifteenth)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_K_fifteenth)
        GL.glBindVertexArray(self.vao_K_sixteenth)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_K_sixteenth)


# Instantiate this class and run the program
Example().run()
