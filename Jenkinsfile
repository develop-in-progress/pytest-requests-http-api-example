pipeline {
    agent any
    parameters {
        string(name: 'TestParameter', defaultValue: 'SomeValue', description: 'Some test value')
    }
    stages {
        stage('Build') {
            steps {
                echo "Building with ${params.TestParameter} parameter"
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