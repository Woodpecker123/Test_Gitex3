pipeline {
  agent any
  stages {
    stage('Check Python Version') {
      steps {
          sh 'python3 --version'
          sh 'pip install sasctl'
      }
    }
     stage('Publish Model') {
      steps {
       
        sh 'python3 ModelPublish.py'
      }
    }

  }
}
