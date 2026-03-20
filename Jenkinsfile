pipeline {
    agent any

    environment {
        BASE_URL = credentials('BASE_URL')
        TEST_USER_EMAIL = credentials('TEST_USER_EMAIL')
        TEST_USER_PASSWORD = credentials('TEST_USER_PASSWORD')
    }

    parameters {
        choice(
            name: 'CAMPAIGN',
            choices: ['smoke', 'regression'],
            description: 'tests campaign which will be run'
        )
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                pip3 install poetry --break-system-packages
                export PATH="/var/jenkins_home/.local/bin:$PATH"
                poetry install
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh """
                 export PATH="/var/jenkins_home/.local/bin:\$PATH"
                 poetry run pytest -m ${params.CAMPAIGN} -v
                 """
            }
        }
    }

    post {
        always {
            echo "Pipeline finalized. Campanign: ${params.CAMPAIGN}"
        }
        success {
            echo "✅ All tests succeeded!"
        }
        failure {
            echo "❌ Some tests failed!"
        }
    }
}