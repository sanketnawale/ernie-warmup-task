import os
import requests
import json
from datetime import datetime

# Your AI Studio token
TOKEN = "8e9e050008f1e71129231efbf6b7e35303da9b07"

def extract_pdf_to_markdown(pdf_path):
    """
    Extract text from PDF using PaddleOCR-VL API
    """
    print("📄 Step 1: Extracting PDF content...")
    
    # API endpoint for PaddleOCR-VL
    url = "https://aistudio.baidu.com/llm/lmapi/v1/chat/file_parsing"
    
    # Prepare the file
    with open(pdf_path, 'rb') as f:
        files = {
            'file': (os.path.basename(pdf_path), f, 'application/pdf')
        }
        
        # Add required date header
        headers = {
            'Authorization': f'token {TOKEN}',
            'x-bce-date': datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
        }
        
        data = {
            'file_type': 'pdf',
            'parse_type': 'markdown'
        }
        
        print("   → Uploading PDF to PaddleOCR-VL API...")
        response = requests.post(url, headers=headers, files=files, data=data, timeout=120)
    
    print(f"   → Response status: {response.status_code}")
    
    if response.status_code == 200:
        result = response.json()
        
        # Extract markdown content
        if 'result' in result:
            markdown_content = result['result'].get('content', '')
            
            # Save markdown to file
            with open('extracted_content.md', 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            
            print("   ✅ PDF extracted successfully!")
            print(f"   → Markdown saved to: extracted_content.md")
            print(f"   → Content length: {len(markdown_content)} characters")
            
            return markdown_content
        else:
            print("   ❌ Error: No result in response")
            print(f"   Response: {result}")
            return None
    else:
        print(f"   ❌ API Error: {response.status_code}")
        print(f"   Response: {response.text}")
        return None

if __name__ == "__main__":
    # Check if PDF exists
    if not os.path.exists('input.pdf'):
        print("❌ Error: input.pdf not found!")
        print("   Please add your PDF file to this folder and name it 'input.pdf'")
    else:
        markdown = extract_pdf_to_markdown('input.pdf')
        
        if markdown:
            print("\n📝 Preview of extracted content:")
            print("=" * 50)
            print(markdown[:500])
            print("=" * 50)
            print("\n🎉 Step 1 Complete! Now run step2_generate_webpage.py")
