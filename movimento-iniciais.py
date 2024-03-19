import OpenGL.GL as GL

from core.base import Base
from core.utils import Utils
from core.attribute import Attribute
from core.uniform import Uniform




class Example(Base):
    def initialize(self):
        print("Initializing program...")
        # Initialize program #
        vs_code = """
            in vec3 position;
            uniform vec3 translation;
            in vec3 position1;
            uniform vec3 translation1;
            void main()
            {
                vec3 pos = position + translation;
                vec3 pos1 = position1 + translation1;
                gl_Position = vec4(pos.x, pos.y, pos.z, 1.0);
                //gl_Position = vec4(pos1.x, pos1.y, pos1.z, 1.0);
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
 


        GL.glClearColor(0.0, 0.0, 0.0, 1.0)

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



        self.vao_Pi_first = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_Pi_first)
        position_Pi_first  = [[0.05,  0.18,  0.0],
                             [0.03,  0.09,  0.0],
                             [0.06,  0.07,  0.0],
                             [0.08,  0.13,  0.0],
                        
                        ]
        self.vertex_count_Pi_first = len(position_Pi_first)
        position_attribute_Pi_first = Attribute('vec3', position_Pi_first)
        position_attribute_Pi_first.associate_variable(self.program_ref, 'position')


        self.vao_Pi_second = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_Pi_second )
        position_Pi_second   = [ [0.07,  0.25,  0.0],
                                [0.05,  0.18,  0.0],
                                [0.08,  0.13,  0.0],
                                [0.09,  0.16,  0.0],
                                [0.1,  0.18,  0.0],
                                [0.12,  0.2,  0.0]]
        self.vertex_count_Pi_second  = len(position_Pi_second )
        position_attribute_Pi_second  = Attribute('vec3', position_Pi_second )
        position_attribute_Pi_second .associate_variable(self.program_ref, 'position') 

        
        self.vao_Pi_third = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_Pi_third )
        position_Pi_third   = [[0.16,  0.31,  0.0],
                              [0.14, 0.31,  0.0],
                              [0.12, 0.3,  0.0],
                              [0.1,  0.29,  0.0],
                              [0.09,  0.27,  0.0],
                              [0.07,  0.25,  0.0],
                              [0.12,  0.2,  0.0],
                              [0.14,  0.21,  0.0],
                              [0.15,  0.22,  0.0],
                              [0.16,  0.22,  0.0],
                              [0.17,  0.23,  0.0],]
        self.vertex_count_Pi_third  = len(position_Pi_third )
        position_attribute_Pi_third  = Attribute('vec3', position_Pi_third )
        position_attribute_Pi_third .associate_variable(self.program_ref, 'position') 


        self.vao_Pi_fourth = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_Pi_fourth )
        position_Pi_fourth   = [[0.55,  0.32,  0.0],
                                [0.3,  0.32,  0.0],
                                [0.26,  0.32,  0.0],
                                [0.21,  0.32,  0.0],
                                [0.18,  0.31,  0.0],
                                [0.16,  0.31,  0.0],
                                [0.17,  0.23,  0.0],
                                [0.24,  0.23,  0.0],
                                [0.4,  0.23,  0.0],
                                [0.55,  0.23,  0.0],]
        self.vertex_count_Pi_fourth  = len(position_Pi_fourth )
        position_attribute_Pi_fourth  = Attribute('vec3', position_Pi_fourth )
        position_attribute_Pi_fourth .associate_variable(self.program_ref, 'position') 



        self.vao_Pi_fifth = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_Pi_fifth )
        position_Pi_fifth   = [[0.37,  0.23,  0.0],
                              [0.32,  0.23,  0.0],
                              [0.31,  0.21,  0.0],
                              [0.3,  0.16,  0.0],
                              [0.28,  0.1,  0.0],
                              [0.34,  0.1,  0.0],
                              [0.34,  0.12,  0.0],
                              [0.36,  0.18,  0.0],]
        self.vertex_count_Pi_fifth  = len(position_Pi_fifth )
        position_attribute_Pi_fifth  = Attribute('vec3', position_Pi_fifth )
        position_attribute_Pi_fifth .associate_variable(self.program_ref, 'position') 

        self.vao_Pi_sixth = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_Pi_sixth )
        position_Pi_sixth   = [[0.34,  0.1,  0.0],
                              [0.28,  0.1,  0.0],
                              [0.26,  0.04,  0.0],
                              [0.24,  -0.03,  0.0],
                              [0.21,  -0.1,  0.0],
                              [0.17,  -0.17,  0.0],
                              [0.25,  -0.19,  0.0],
                              [0.28,  -0.1,  0.0],
                              [0.3,  -0.03,  0.0],
                              [0.32,  0.04,  0.0],]
        self.vertex_count_Pi_sixth = len(position_Pi_sixth )
        position_attribute_Pi_sixth  = Attribute('vec3', position_Pi_sixth )
        position_attribute_Pi_sixth .associate_variable(self.program_ref, 'position') 


        self.vao_Pi_seventh = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_Pi_seventh )
        position_Pi_seventh   = [[0.25,  -0.19,  0.0],
                              [0.17,  -0.17,  0.0],
                              [0.16,  -0.2,  0.0],
                              [0.14, -0.23,  0.0],
                              [0.12,  -0.28,  0.0],
                              [0.21,  -0.3,  0.0],
                              [0.22,  -0.26,  0.0],
                              [0.23,  -0.23,  0.0],]
        self.vertex_count_Pi_seventh = len(position_Pi_seventh )
        position_attribute_Pi_seventh  = Attribute('vec3', position_Pi_seventh )
        position_attribute_Pi_seventh .associate_variable(self.program_ref, 'position') 


        self.vao_Pi_eighth = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_Pi_eighth )
        position_Pi_eighth   = [[0.21, -0.3,  0.0],
                                [0.12, -0.28,  0.0],
                              [0.12,  -0.29,  0.0],
                              [0.19,  -0.31,  0.0],]
        self.vertex_count_Pi_eighth = len(position_Pi_eighth )
        position_attribute_Pi_eighth  = Attribute('vec3', position_Pi_eighth )
        position_attribute_Pi_eighth .associate_variable(self.program_ref, 'position') 

        self.vao_Pi_ninth = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_Pi_ninth )
        position_Pi_ninth   = [[0.7,  0.32,  0.0],
                              [0.65,  0.32,  0.0],
                              [0.55,  0.32,  0.0],
                              [0.5,  0.23,  0.0],
                              [0.66,  0.23,  0.0],
                              [0.69,  0.23,  0.0],
                              [0.7,  0.23,  0.0],]
        self.vertex_count_Pi_ninth = len(position_Pi_ninth )
        position_attribute_Pi_ninth  = Attribute('vec3', position_Pi_ninth )
        position_attribute_Pi_ninth .associate_variable(self.program_ref, 'position') 


        self.vao_Pi_tenth = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_Pi_tenth )
        position_Pi_tenth   = [[0.67,  0.24,  0.0],
                                [0.56,  0.23,  0.0],
                              [0.57,  0.22,  0.0],
                              [0.65,  0.22,  0.0],]
        self.vertex_count_Pi_tenth = len(position_Pi_tenth )
        position_attribute_Pi_tenth  = Attribute('vec3', position_Pi_tenth  )
        position_attribute_Pi_tenth.associate_variable(self.program_ref, 'position') 

        self.vao_Pi_eleventh = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_Pi_eleventh )
        position_Pi_eleventh   = [[0.65,  0.22,  0.0],
                                [0.57,  0.22,  0.0],
                                [0.56,  0.18,  0.0],
                                [0.56,  0.13,  0.0],
                                [0.64,  0.18,  0.0],
                                 ]
        self.vertex_count_Pi_eleventh = len(position_Pi_eleventh )
        position_attribute_Pi_eleventh  = Attribute('vec3', position_Pi_eleventh  )
        position_attribute_Pi_eleventh.associate_variable(self.program_ref, 'position') 

        self.vao_Pi_twelfth = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_Pi_twelfth )
        position_Pi_twelfth   = [[0.64  ,  0.2,  0.0],
                                [0.56,  0.13,  0.0],
                                [0.56,  0.07,  0.0],
                                [0.55,  0.01,  0.0],
                                [0.55,  -0.05,  0.0],
                                [0.55,  -0.1,  0.0],
                                [0.65,  -0.1,  0.0],
                                [0.64,  -0.07,  0.0],
                                [0.64,  -0.01,  0.0],
                                [0.64,  0.05,  0.0],]
        self.vertex_count_Pi_twelfth = len(position_Pi_twelfth )
        position_attribute_Pi_twelfth  = Attribute('vec3', position_Pi_twelfth  )
        position_attribute_Pi_twelfth.associate_variable(self.program_ref, 'position') 


        self.vao_Pi_thirteenth = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_Pi_thirteenth )
        position_Pi_thirteenth   = [[0.65,  -0.1,  0.0],
                                [0.55,  -0.1,  0.0],
                                [0.55,  -0.15,  0.0],
                                [0.55,  -0.21,  0.0],
                                [0.67,  -0.18,  0.0],
                                [0.66,  -0.15,  0.0],
                                [0.65,  -0.13,  0.0],
                                ]
        self.vertex_count_Pi_thirteenth = len(position_Pi_thirteenth )
        position_attribute_Pi_thirteenth  = Attribute('vec3', position_Pi_thirteenth  )
        position_attribute_Pi_thirteenth.associate_variable(self.program_ref, 'position')

        self.vao_Pi_fourteenth = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_Pi_fourteenth )
        position_Pi_fourteenth   = [[0.67,  -0.18,  0.0],
                                   [0.55, -0.21,  0.0],
                                   [0.56, -0.25,  0.0],
                                   [0.58, -0.28,  0.0],
                                   [0.6, -0.29,  0.0],
                                   [0.7, -0.21,  0.0],
                                   [0.68, -0.2,  0.0],
                                   [0.67, -0.19,  0.0],]
        self.vertex_count_Pi_fourteenth = len(position_Pi_fourteenth )
        position_attribute_Pi_fourteenth  = Attribute('vec3', position_Pi_fourteenth  )
        position_attribute_Pi_fourteenth.associate_variable(self.program_ref, 'position')

        self.vao_Pi_fifteenth = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_Pi_fifteenth )
        position_Pi_fifteenth   = [[0.73,  -0.22,  0.0],
                                   [0.71, -0.22,  0.0],
                                   [0.7, -0.21,  0.0],
                                   [0.6, -0.29,  0.0],
                                   [0.62, -0.3,  0.0],
                                   [0.65, -0.31,  0.0],
                                   [0.69, -0.3,  0.0],]
        self.vertex_count_Pi_fifteenth = len(position_Pi_fifteenth )
        position_attribute_Pi_fifteenth  = Attribute('vec3', position_Pi_fifteenth  )
        position_attribute_Pi_fifteenth.associate_variable(self.program_ref, 'position')
        

        self.vao_Pi_sixteenth = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_Pi_sixteenth )
        position_Pi_sixteenth   = [[0.79, -0.2,  0.0],
                                   [0.77,  -0.21,  0.0],
                                   [0.75, -0.22,  0.0],
                                   [0.73, -0.22,  0.0],
                                   [0.69, -0.3,  0.0],
                                   [0.72, -0.29,  0.0],
                                   [0.76, -0.27,  0.0],
                                   [0.78, -0.26,  0.0],
                                   [0.81, -0.22,  0.0],
                                   ]
        self.vertex_count_Pi_sixteenth = len(position_Pi_sixteenth )
        position_attribute_Pi_sixteenth  = Attribute('vec3', position_Pi_sixteenth  )
        position_attribute_Pi_sixteenth.associate_variable(self.program_ref, 'position')

        self.vao_Pi_seventeenth = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_Pi_seventeenth )
        position_Pi_seventeenth   = [[0.8, 0.34,  0.0],
                                   [0.76,  0.32,  0.0],
                                   [0.7, 0.32,  0.0],
                                   [0.7, 0.23,  0.0],
                                   [0.76, 0.25,  0.0],
                                   [0.8, 0.26,  0.0],]
        self.vertex_count_Pi_seventeenth = len(position_Pi_seventeenth )
        position_attribute_Pi_seventeenth  = Attribute('vec3', position_Pi_seventeenth  )
        position_attribute_Pi_seventeenth.associate_variable(self.program_ref, 'position')


        self.vao_Pi_eighteenth = GL.glGenVertexArrays(1)
        GL.glBindVertexArray(self.vao_Pi_eighteenth )
        position_Pi_eighteenth   = [[0.84, 0.36,  0.0],
                                   [0.82,  0.34,  0.0],
                                   [0.8,   0.34,  0.0],
                                   [0.8, 0.26,  0.0],
                                   [0.81, 0.28,  0.0],
                                   [0.83, 0.3,  0.0],
                                   [0.85, 0.35,  0.0],
                                   ]
        self.vertex_count_Pi_eighteenth = len(position_Pi_eighteenth )
        position_attribute_Pi_eighteenth  = Attribute('vec3', position_Pi_eighteenth  )
        position_attribute_Pi_eighteenth.associate_variable(self.program_ref, 'position')

        # Set up uniforms #
        self.translation = Uniform('vec3', [0.0, 0.0, 0.0])
        self.translation.locate_variable(self.program_ref, 'translation')
        self.translation0 = [0.0,0.0,0.0]
        self.translation1 = [0.0,0.0,0.0]
        self.base_color = Uniform('vec3', [0.0, 1.0, 0.0])
        self.base_color.locate_variable(self.program_ref, 'baseColor')
        self.selecionado_K = 0
        self.selecionado_Pi = 0


    def print_K_first(self):
        self.translation.data = self.translation0
        if self.selecionado_K == 0:
            self.base_color.data[2] = 0.0
            self.base_color.data[1] = 1.0
            self.base_color.data[0] = 1.0
        else:
            self.base_color.data[2] = 0.0
            self.base_color.data[1] = 0.7
            self.base_color.data[0] = 0.0


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


    def print_Pi_first(self):
        self.translation.data = self.translation1
        if self.selecionado_Pi == 0:
            self.base_color.data[2] = 0.0
            self.base_color.data[1] = 1.0
            self.base_color.data[0] = 1.0
        else:
            self.base_color.data[2] = 1.0
            self.base_color.data[1] = 0.0
            self.base_color.data[0] = 0.0
        self.translation.upload_data()
        self.base_color.upload_data()

        GL.glBindVertexArray(self.vao_Pi_first)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_Pi_first)
        GL.glBindVertexArray(self.vao_Pi_second)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_Pi_second)
        GL.glBindVertexArray(self.vao_Pi_third)
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_Pi_third)
        GL.glBindVertexArray(self.vao_Pi_fourth )
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_Pi_fourth)
        GL.glBindVertexArray(self.vao_Pi_fifth )
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_Pi_fifth )
        GL.glBindVertexArray(self.vao_Pi_sixth )
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_Pi_sixth )
        GL.glBindVertexArray(self.vao_Pi_seventh )
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_Pi_seventh )
        GL.glBindVertexArray(self.vao_Pi_eighth )
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_Pi_eighth )
        GL.glBindVertexArray(self.vao_Pi_ninth )
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_Pi_ninth )
        GL.glBindVertexArray(self.vao_Pi_tenth )
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_Pi_tenth )
        GL.glBindVertexArray(self.vao_Pi_eleventh )
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_Pi_eleventh )
        GL.glBindVertexArray(self.vao_Pi_twelfth )
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_Pi_twelfth )
        GL.glBindVertexArray(self.vao_Pi_thirteenth )
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_Pi_thirteenth )
        GL.glBindVertexArray(self.vao_Pi_fourteenth )
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_Pi_fourteenth )
        GL.glBindVertexArray(self.vao_Pi_fifteenth )
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_Pi_fifteenth )
        GL.glBindVertexArray(self.vao_Pi_sixteenth )
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_Pi_sixteenth )
        GL.glBindVertexArray(self.vao_Pi_seventeenth )
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_Pi_seventeenth )
        GL.glBindVertexArray(self.vao_Pi_eighteenth )
        GL.glDrawArrays(GL.GL_TRIANGLE_FAN , 0, self.vertex_count_Pi_eighteenth)
        


    def update(self):
        """ Update data """

        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        GL.glUseProgram(self.program_ref)


        if self.input.letra%2  == 1:
            if self.input.move_right == 1:
                self.translation0[0] += 0.01

            if self.input.move_left == 1:
                self.translation0[0] -= 0.01

            if self.input.move_up == 1:
               self.translation0[1] += 0.01
            
            if self.input.move_down == 1:
                self.translation0[1] -= 0.01
    
        if self.input.letra%2 == 0:
            if self.input.move_right == 1:
                self.translation1[0] += 0.01
            
            if self.input.move_left == 1:
                self.translation1[0] -= 0.01
            
            if self.input.move_up == 1:
                self.translation1[1] += 0.01
            
            if self.input.move_down == 1:
                self.translation1[1] -= 0.01


        if self.input.letra%2  == 0:
            self.selecionado_K = 1
            self.selecionado_Pi = 0
            self.print_K_first()
            self.print_Pi_first()

        if self.input.letra%2  == 1:
            self.selecionado_K = 0
            self.selecionado_Pi = 1
            self.print_Pi_first()
            self.print_K_first()

    


        
    
    

# Instantiate this class and run the program
Example().run()
