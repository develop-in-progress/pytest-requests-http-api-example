pipeline {
    agent any
    parameters {
        string(name: 'TestParameter', defaultValue: 'SomeValue', description: 'Some test value')
    }
    stages {
        stage('Parameters'){
                steps {
                    script {
                    properties([
                            parameters([
                                [$class: 'ChoiceParameter',
                                    choiceType: 'PT_SINGLE_SELECT',
                                    description: 'Select the Environemnt from the Dropdown List',
                                    filterLength: 1,
                                    filterable: false,
                                    name: 'Env',
                                    script: [
                                        $class: 'GroovyScript',
                                        fallbackScript: [
                                            classpath: [],
                                            sandbox: false,
                                            script:
                                                "return['Could not get The environemnts']"
                                        ],
                                        script: [
                                            classpath: [],
                                            sandbox: false,
                                            script:
                                                "return['dev','stage','prod']"
                                        ]
                                    ]
                                ],
                                [$class: 'CascadeChoiceParameter',
                                    choiceType: 'PT_SINGLE_SELECT',
                                    description: 'Select the AMI from the Dropdown List',
                                    name: 'List',
                                    referencedParameters: 'Env',
                                    script:
                                        [$class: 'GroovyScript',
                                        fallbackScript: [
                                                classpath: [],
                                                sandbox: false,
                                                script: "return['Could not get Environment from Env Param']"
                                                ],
                                        script: [
                                                classpath: [],
                                                sandbox: false,
                                                script: '''
                                                if (Env.equals("dev")){
                                                    return["param1", "param2", "param3"]
                                                }
                                                else if(Env.equals("stage")){
                                                    return["param4", "param5", "param6"]
                                                }
                                                else if(Env.equals("prod")){
                                                    return["param7", "param8", "param9"]
                                                }
                                                '''
                                            ]
                                    ]
                                ],
                                [$class: 'DynamicReferenceParameter',
                                    choiceType: 'ET_ORDERED_LIST',
                                    description: 'Select the  AMI based on the following infomration',
                                    name: 'Image Information',
                                    referencedParameters: 'Env',
                                    script:
                                        [$class: 'GroovyScript',
                                        script: 'return["Could not get AMi Information"]',
                                        script: [
                                                script: '''
                                                if (Env.equals("dev")){
                                                    return["param1", "param2", "param3"]
                                                }
                                                else if(Env.equals("stage")){
                                                    return["param4", "param5", "param6"]
                                                }
                                                else if(Env.equals("prod")){
                                                    return["param7", "param8", "param9"]
                                                }
                                                '''
                                                ]
                                        ]
                                ]
                            ])
                        ])
                    }
                }
            }
        stage('Build') {
            steps {
                echo "${params.TestParameter} !"
            }
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 --version'
                sh 'pip3 install -r requirements.txt'
                sh 'python3 -m pytest --alluredir=allure-results'
            }
        }
        stage('Reports') {
            steps {
            script {
            allure([
                    includeProperties: false,
                    jdk: '',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'allure-results']]
                    ])
                }
                }
            }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}

pipeline {
    agent any
        stages {

        }
}